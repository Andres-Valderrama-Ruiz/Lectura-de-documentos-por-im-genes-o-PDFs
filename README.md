\## 📌 Descripción



Este proyecto implementa una \*\*API REST HTTP\*\* que:

\- Recibe documentos de identificación (\*\*Cédulas\*\*, \*\*Pasaportes\*\*, etc.) en imagen o PDF.

\- Extrae texto legible mediante \*\*OCR (Tesseract + OpenCV)\*\*.

\- Clasifica automáticamente el tipo de documento.

\- Guarda la información estructurada en \*\*MySQL\*\*.



-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



\## 📁 Estructura del Proyecto



extractor\_docs/

│

├── app/

│ ├── main.py 

│ ├── services.py 

│ ├── database.py

│ ├── init.py

│

├── requirements.txt

├── README.md

├── venv





\## ✅ Requisitos previos



\### 🛠️ 1️⃣ Instalar Python

Versión recomendada: \*\*3.10+\*\*



\### 🔍 2️⃣ Instalar Tesseract OCR



\- \*\*Windows:\*\*  

&nbsp; Descargar el instalador oficial:

&nbsp; \[https://github.com/tesseract-ocr/tesseract] Una vez descargado identificar la ruta donde se dejara la carpeta Tesseract-OCR porque se requiere su ejecutable tesseract.exe para agregar la ruta al PATH, una vez identificada la ruta se agrega la ruta al PATH.



&nbsp; Ejemplo de ruta:

C:\\Program Files\\Tesseract-OCR\\tesseract.exe





\### 📄 3️⃣ Instalar Poppler (para PDFs)



\- \*\*Windows:\*\*  

Descargar compilación:

\[https://poppler.freedesktop.org/] o \[https://github.com/oschwartz10612/poppler-windows]



Como el paso anterior se descomprime y agrega la carpeta `/bin` al PATH.



----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



\## 🗃️ Variables de entorno (Base de datos MySQL)


Primero se debe instalar y configurar MySQL

Posteriormente se debe crear la base de datos destino, sino se tiene una o si se quiere crear otra usar el comando: CREATE DATABASE Nombre;



Ejemplo:
CREATE DATABASE documentos\_db;



Una vez creada o seleccionada que base de datos se va a utilizar, se debe crear la tabla que almacenara la información de la lectura de documentos. Para esto, ejecutar en el gestor de base de datos el siguiente script:

CREATE TABLE documentos (

&nbsp;   id INT AUTO\_INCREMENT PRIMARY KEY,

&nbsp;   tipo\_documento VARCHAR(50),

&nbsp;   texto LONGTEXT

);



Esto crea las columnas deseadas junto con un id auto-incremental.


Ir al archivo database.py y reemplaza base de datos, usuario, contraseña y base de datos mediante variables de entorno.



&nbsp;	    host="localhost",

&nbsp;           user="root",

&nbsp;           password="password",

&nbsp;           database="documentos\_db"



-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



🚀 Ejecutar el servicio

Levanta la API:

en el bash, ejeutar el siguiente comando:


uvicorn app.main:app --reload



-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



📮 Prueba con Postman

1️⃣ Abre Postman



2️⃣ Nueva solicitud POST a:



http://127.0.0.1:8000/extract



3️⃣ Body → form-data:

LLenar el KEY de la siguiente manera:



Key: file → Type: File → Selecciona imagen o PDF

Solo requiere un KEY, luego se envia la solicitud



4️⃣ Salida:

El resultado esperado por postman sera algo similar a esto:


{

&nbsp; "tipo\_documento": "Cédula",

&nbsp; "texto\_extraido": "..."

}

Ya debería estar almacenada la información extraída de los documentos en la base de datos MySQL.

