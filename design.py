import subprocess
import random
import torch
import numpy as np
from PIL import Image
import nodes
from nodes import NODE_CLASS_MAPPINGS
from totoro_extras import nodes_custom_sampler
from totoro import model_management

# Directory changes and cloning
subprocess.run(["git", "clone", "-b", "totoro3", "https://github.com/camenduru/ComfyUI", "/content/TotoroUI"], check=True)

# Installing necessary libraries
subprocess.run(["pip", "install", "-q", "torchsde", "einops", "diffusers", "accelerate", "xformers==0.0.28.post2"], check=True)
subprocess.run(["apt", "-y", "install", "-qq", "aria2"], check=True)

# Downloading files using aria2c
subprocess.run([
    "aria2c", "--console-log-level=error", "-c", "-x", "16", "-s", "16", "-k", "1M",
    "https://huggingface.co/camenduru/FLUX.1-dev/resolve/main/flux1-dev-fp8.safetensors",
    "-d", "/content/TotoroUI/models/unet", "-o", "flux1-dev-fp8.safetensors"
], check=True)

subprocess.run([
    "aria2c", "--console-log-level=error", "-c", "-x", "16", "-s", "16", "-k", "1M",
    "https://huggingface.co/camenduru/FLUX.1-dev/resolve/main/ae.sft",
    "-d", "/content/TotoroUI/models/vae", "-o", "ae.sft"
], check=True)

subprocess.run([
    "aria2c", "--console-log-level=error", "-c", "-x", "16", "-s", "16", "-k", "1M",
    "https://huggingface.co/camenduru/FLUX.1-dev/resolve/main/clip_l.safetensors",
    "-d", "/content/TotoroUI/models/clip", "-o", "clip_l.safetensors"
], check=True)

subprocess.run([
    "aria2c", "--console-log-level=error", "-c", "-x", "16", "-s", "16", "-k", "1M",
    "https://huggingface.co/camenduru/FLUX.1-dev/resolve/main/t5xxl_fp8_e4m3fn.safetensors",
    "-d", "/content/TotoroUI/models/clip", "-o", "t5xxl_fp8_e4m3fn.safetensors"
], check=True)

# Loading models and initializing nodes
DualCLIPLoader = NODE_CLASS_MAPPINGS["DualCLIPLoader"]()
UNETLoader = NODE_CLASS_MAPPINGS["UNETLoader"]()
RandomNoise = nodes_custom_sampler.NODE_CLASS_MAPPINGS["RandomNoise"]()
BasicGuider = nodes_custom_sampler.NODE_CLASS_MAPPINGS["BasicGuider"]()
KSamplerSelect = nodes_custom_sampler.NODE_CLASS_MAPPINGS["KSamplerSelect"]()
BasicScheduler = nodes_custom_sampler.NODE_CLASS_MAPPINGS["BasicScheduler"]()
SamplerCustomAdvanced = nodes_custom_sampler.NODE_CLASS_MAPPINGS["SamplerCustomAdvanced"]()
VAELoader = NODE_CLASS_MAPPINGS["VAELoader"]()
VAEDecode = NODE_CLASS_MAPPINGS["VAEDecode"]()
EmptyLatentImage = NODE_CLASS_MAPPINGS["EmptyLatentImage"]()

with torch.no_grad():
    clip = DualCLIPLoader.load_clip("t5xxl_fp8_e4m3fn.safetensors", "clip_l.safetensors", "flux")[0]
    unet = UNETLoader.load_unet("flux1-dev-fp8.safetensors", "fp8_e4m3fn")[0]
    vae = VAELoader.load_vae("ae.sft")[0]

# Helper function to find the closest number
def closestNumber(n, m):
    q = int(n / m)
    n1 = m * q
    if (n * m) > 0:
        n2 = m * (q + 1)
    else:
        n2 = m * (q - 1)
    return n1 if abs(n - n1) < abs(n - n2) else n2
