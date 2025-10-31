
// ----  Definiendo pines
// Entradas digitales
int DI_00 = 32;
int DI_01 = 33;
int DI_02 = 25;

// Salidas Digitales
int DO_00 = 19;
int DO_01 = 18;
int DO_02 = 5;
int DO_03 = 2;

// ---- Variables Internas
byte X_00;
byte X_01;
byte X_02;

byte Y_00;
byte Y_01;
byte Y_02;
byte Y_03;

const int numero_M = 8;
byte M[numero_M];

// ---- Temporizadores

#define  numeroDeTON 16
struct temporizador {
    byte entrada;
    byte salida;
    unsigned long tiempo;
    unsigned long tiempoActual;
} TON[numeroDeTON];
struct temporizadorAux {
    byte bandera;
    unsigned long tiempo_Aux1;
    unsigned long tiempo_Aux2;
} TON_Aux[numeroDeTON];

void actualizarTON (int);


// Contadores

#define numeroDeContadores 8
struct contador {
    byte entrada;
    byte salida;
    byte habilitar;
    int cuentaActual;
    int cuentaMaxima;
    byte reset;
    byte aux1;
    byte aux2;
} C[numeroDeContadores];
void actualizarContador (byte);

// Comunicacion
#define bufferIndiceMaximo 20
byte bufferLectura[bufferIndiceMaximo];
int bufferIndice = 0;

byte bufferInstruccion[bufferIndiceMaximo];
int bufferIndiceInstruccion = 0;

void colocarEnBufferDatosSerial();
void imprimirTrama(byte *, int , int );
void leerInstruccionesDeBuffer(byte *, int *, byte *, int *);

char caracterInicio = '*';
char caracterFin = '_';

// Parametros de comunicacion

#define CONTROL 49 // '1'
#define ADMINISTRACION 50 // '2'

#define SOLICITUD_MODIFICAR_BANDERA 49 // '1' 

void obtenerInstruccion();

void setup() {
  // Configurando pines
  pinMode(DI_00, INPUT);
  pinMode(DI_01, INPUT);
  pinMode(DI_02, INPUT);
  
  pinMode(DO_00, OUTPUT);
  pinMode(DO_01, OUTPUT);
  pinMode(DO_02, OUTPUT);
  pinMode(DO_03, OUTPUT);
  
  
  // Configurando temporizadores
  TON[0].tiempo = (unsigned long)1 * 5000;
  TON[1].tiempo = (unsigned long)1 * 700;
  TON[2].tiempo = (unsigned long)1 * 300;
  TON[3].tiempo = (unsigned long)1 * 2000;

  // Configurando Contadores  
  C[0].cuentaMaxima = 3;

  // Cnfigurando comunicacion Serie
  Serial.begin(115200, SERIAL_8N1);
}

void loop() {
  // Código para comunicación
  //Serial.print("Enviando datos\n"); 
  colocarEnBufferDatosSerial();
  leerInstruccionesDeBuffer(bufferLectura, &bufferIndice, bufferInstruccion, &bufferIndiceInstruccion);
  
  
  // Codigo principal 
  
  M[0] =(X_00 || M[0])&&!X_01;
  
  TON[0].entrada = M[0] && !TON[3].salida;
  actualizarTON(0);

  TON[1].entrada = M[0] && TON[0].salida;
  actualizarTON(1);

  TON[2].entrada = M[0] && TON[1].salida;
  actualizarTON(2);

  TON[3].entrada = M[0] && TON[2].salida;
  actualizarTON(3);

  // Rojo
  Y_00 = M[0] && !TON[0].salida;

  // Amarillo
  // Parpadeo
  M[1] = !TON[1].salida;
  Y_01 = M[0] && TON[0].salida && M[1];

  // Verde
  Y_02 = M[0] && TON[1].salida && TON[0].salida ;

  Y_03 = M[1];
  

  // C[0].habilitar =  1; // Señal para habilitar el funcionamiento del contador
  // C[0].entrada = #; // Se describe aqui la señal que contine los pulsos de entrada
  // actualizarContador(0);



  // Leyendo entradas y escribiendo salidas
  X_00 = digitalRead(DI_00);
  X_01 = digitalRead(DI_01);
  X_02 = digitalRead(DI_02);
  
  digitalWrite(DO_00, Y_00);
  digitalWrite(DO_01, Y_01);
  digitalWrite(DO_02, Y_02);
  digitalWrite(DO_03, Y_03);
}


void actualizarTON (int i) {
     if (TON [i].entrada)
   {
        if (!TON_Aux[i].bandera) {
           TON_Aux[i].bandera = true;
           TON_Aux[i].tiempo_Aux1 = millis ();  
        }
        TON_Aux[i].tiempo_Aux2 = millis ();
        TON [i].tiempoActual = TON_Aux[i].tiempo_Aux2 - TON_Aux[i].tiempo_Aux1;

        if (TON [i].tiempoActual > TON [i].tiempo) {
            TON [i].salida = true;
        }
    } else {
        TON [i].salida = false;
        TON_Aux[i].bandera = false;
    }
}
// Contadores
void actualizarContador (byte numeroContador) {

    if (!C[numeroContador].habilitar) {
        C[numeroContador].salida = 0;
        C[numeroContador].cuentaActual = 0;
    } else {
        C[numeroContador].aux2 = C[numeroContador].aux1 & !C[numeroContador].entrada;
    
        if (C[numeroContador].aux2) {
            if (C[numeroContador].cuentaActual < C[numeroContador].cuentaMaxima){
              C[numeroContador].cuentaActual++;
            }

        }
    }
    
    if (C[numeroContador].reset) {
        C[numeroContador].cuentaActual = 0;
    }
    if (C[numeroContador].cuentaActual >= C[numeroContador].cuentaMaxima ) {
        C[numeroContador].salida = 1;
    } else {
        C[numeroContador].salida = 0;
    }
    
    C[numeroContador].aux1 = C[numeroContador].entrada;
    C[numeroContador].reset = 0;
}






// Comunicacion

void colocarEnBufferDatosSerial() {
  byte caracter;
  int aux = 0;

  while(Serial.available()) {
    caracter = Serial.read();
    bufferLectura[bufferIndice++] = caracter;

    if (bufferIndice + 1 > bufferIndiceMaximo) {
      aux = bufferIndiceMaximo >> 1;

      for (int i = aux; i <bufferIndiceMaximo + 1; i++) {
        bufferIndice = i - aux;
        bufferLectura[bufferIndice] = bufferLectura[i];
      }
    }

    // Probando que almacenamos datos
    // imprimirTrama(bufferLectura, 0, bufferIndice);
  }
}

void leerInstruccionesDeBuffer(byte *ptrBufferLectura, int *ptrBufferIndice, 
  byte *ptrBufferInstruccion, int *ptrTamanioBufferInstruccion){

  int i = 0;
  int k = 0;
  int encontrado = -1;

  if (ptrBufferLectura[*ptrBufferIndice -1 ] == caracterFin){
    for (k = *ptrBufferIndice; k >= 0; --k){
      if (ptrBufferLectura[k] == (byte) caracterInicio) {
        encontrado = k;
        
        // Si se encontro el caracter de inicio realizamos la copia de la instruccion
        if (encontrado >= 0) {
          *ptrTamanioBufferInstruccion = 0;
          for (int j = k; j < *ptrBufferIndice; j++)   {
            ptrBufferInstruccion[*ptrTamanioBufferInstruccion] = ptrBufferLectura[j];
            (*ptrTamanioBufferInstruccion)++;
          }
          imprimirTrama(ptrBufferInstruccion, 0, *ptrTamanioBufferInstruccion);
          *ptrBufferIndice = 0;

          obtenerInstruccion();
        }
      }
    }
  }
}

void obtenerInstruccion(){
  int *tamanio;
  byte *cadena;

  int tipoDeInstruccion = 0;
  int numeroDeInstruccion = 0;

  tamanio = &bufferIndiceInstruccion;
  cadena =  bufferInstruccion;

  tipoDeInstruccion = obtenerByteDeArregloByte(cadena + 1);
  numeroDeInstruccion = obtenerByteDeArregloByte(cadena + 2 );
  
  Serial.print("\ntipo: ");
  Serial.write(tipoDeInstruccion);
  Serial.print(",   numero: ");
  Serial.write(numeroDeInstruccion);
}

byte obtenerByteDeArregloByte(byte* arreglo) {
  byte *puntero;
  puntero = (byte *) arreglo;
  return *puntero;
}

int obtenerIntDeArregloByte(byte* arreglo) {
  int *puntero;
  puntero = (int *) arreglo;
  return *puntero;
}


void imprimirTrama(byte *ptrTrama, int inicio, int tamanio) {
  for(int k = inicio; k <inicio + tamanio; k++) {
    Serial.write(ptrTrama[k]);
  }
  Serial.print("\n");
}
