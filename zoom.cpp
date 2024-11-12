#include <QCoreApplication>
#include <QFileInfo>
#include <QDebug>

int main(int argc, char *argv[]) {
    QCoreApplication app(argc, argv);

    // मान लीजिये एक फाइल पाथ है
    QString filePath = "/path/to/your/file.txt";
    QFileInfo fileInfo(filePath);

    if (fileInfo.exists()) {
        qDebug() << "File Name:" << fileInfo.fileName();
        qDebug() << "File Path:" << fileInfo.filePath();
        qDebug() << "Base Name:" << fileInfo.baseName();
        qDebug() << "Extension:" << fileInfo.suffix();
        qDebug() << "Size:" << fileInfo.size() << "bytes";
        qDebug() << "Is Readable:" << fileInfo.isReadable();
        qDebug() << "Is Writable:" << fileInfo.isWritable();
        qDebug() << "Last Modified:" << fileInfo.lastModified();
    } else {
        qDebug() << "The file does not exist.";
    }

    return 0;
}
