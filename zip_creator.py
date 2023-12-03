
import zipfile
import pathlib

def make_archive(filepaths, destinationPath, nameZippedFile):

    destinationPath = pathlib.Path(destinationPath, nameZippedFile)

    with zipfile.ZipFile(destinationPath, "w", zipfile.ZIP_DEFLATED) as archive:
        
        for file in filepaths:
            # estraiamo il file col suo nome, escludendo il percorso
            file = pathlib.Path(file)
            archive.write(file, arcname=file.name)

if __name__ == "__main__":
    print("ciao")