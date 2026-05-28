
raw
Readme · MD
# Calculadora Científica Graficadora
 
Proyecto final — Calculadora en consola desarrollada en Python que implementa operaciones básicas, funciones científicas con métodos de aproximación propios, evaluación y graficación de funciones en la terminal, e historial de operaciones.
 
---
 
## Requisitos
 
- Python 3.8 o superior
- No requiere librerías externas (todo funciona con Python puro)
---
 
## Estructura del proyecto
 
```
Proyecto_final/
├── Main.py                    # Punto de entrada y menús del programa
├── Operaciones_Basicas.py     # Suma, resta, multiplicación, división, potencia
├── Operaciones_Cientificas.py # Factorial, raíz, exponencial, seno, coseno, logaritmo
├── Graficadora.py             # Graficación de funciones en consola
├── Historial.py               # Registro de operaciones realizadas
└── README.md                  # Este archivo
```
 
---
 
## Instrucciones de uso
 
### 1. Ejecución
 
Desde la terminal, ubíquese en la carpeta del proyecto y ejecute:
 
```bash
python Main.py
```
 
### 2. Menú principal
 
Al iniciar, verá el siguiente menú:
 
```
   CALCULADORA CIENTIFICA GRAFICADORA
----------------------------------------
1. Operaciones basicas
2. Operaciones científicas
3. Evaluar una funcion
4. Graficar una funcion en consola
5. Ver historial de operaciones
6. Salir
```
 
Ingrese el número de la opción deseada y presione **Enter**.
 
### 3. Operaciones básicas
 
Incluye: **suma, resta, multiplicación, división y potencia**.
 
- Para suma, resta, multiplicación y división: ingrese dos números reales.
- Para potencia: ingrese la base (real) y el exponente (entero ≥ 0).
- La división por cero y exponentes negativos muestran mensajes de error y regresan al menú.
### 4. Operaciones científicas
 
Incluye: **factorial, raíz cuadrada, exponencial (eˣ), seno, coseno y logaritmo natural**.
 
- Factorial: requiere un entero ≥ 0.
- Raíz cuadrada: requiere un número ≥ 0.
- Seno y coseno: el ángulo debe ingresarse **en radianes**.
- Logaritmo natural: requiere un número **x > 0**.
- Los resultados se muestran con dos decimales de precisión.
### 5. Evaluar una función f(x)
 
Permite evaluar una de las siguientes funciones predefinidas en un valor x:
 
| Opción | Función |
|--------|---------|
| 1 | Lineal: f(x) = 2x + 1 |
| 2 | Cuadrática: f(x) = x² |
| 3 | Cúbica: f(x) = x³ |
| 4 | Mixta: f(x) = x² + 2x + 1 |
 
### 6. Graficar una función en consola
 
Dibuja la gráfica de una función directamente en la terminal usando caracteres `*`.
 
Funciones disponibles: `lineal`, `cuadratica`, `cubica`, `seno_aprox`
 
Ejemplo de uso:
```
Escriba el nombre de la funcion: cuadratica
Valor inicial de x (ejemplo -5): -3
Valor final de x   (ejemplo  5): 3
```
 
El programa valida que el valor inicial sea menor que el final.
 
### 7. Ver historial
 
Muestra todas las operaciones realizadas en la sesión actual, numeradas en orden cronológico.
 
---
 
## Métodos de aproximación utilizados
 
Todas las funciones científicas fueron implementadas **desde cero**, sin usar el módulo `math` de Python. A continuación se explica cada método empleado.
 
### Potencia entera — Multiplicación iterativa
 
Para calcular `base^exponente` con exponente entero ≥ 0, se realizan multiplicaciones sucesivas:
 
```
resultado = 1
repetir 'exponente' veces: resultado = resultado × base
```
 
Esto implementa directamente la definición de potencia como multiplicación repetida. No requiere aproximación ya que opera sobre valores exactos.
 
### Factorial — Producto iterativo
 
El factorial de n (n!) se calcula multiplicando todos los enteros de 1 hasta n:
 
```
resultado = 1
para i desde 1 hasta n: resultado = resultado × i
```
 
Al igual que la potencia, es un cálculo exacto mediante iteración simple.
 
### Raíz cuadrada — Método de Newton-Raphson (Método de Herón)
 
Para calcular √n, se parte de una estimación inicial (`n/2`) y se refina iterativamente usando la fórmula:
 
```
estimacion = (estimacion + n / estimacion) / 2
```
 
Este proceso se repite 50 veces. Cada iteración acerca la estimación a la raíz verdadera de forma cuadrática (los decimales correctos se duplican en cada paso), logrando una precisión muy alta en pocas iteraciones.
 
**Ejemplo:** para √2, desde estimacion=1.0 se obtiene rápidamente 1.41421356...
 
### Exponencial — Serie de Taylor de eˣ
 
La función e^x se calcula sumando los primeros 50 términos de su serie de Taylor:
 
```
e^x = 1 + x + x²/2! + x³/3! + x⁴/4! + ...
```
 
El programa acumula los términos de forma eficiente: en lugar de recalcular cada factorial, el término siguiente se obtiene multiplicando el anterior por `x/i`. Con 50 términos se obtiene una precisión excelente para la mayoría de valores de x.
 
### Seno — Serie de Taylor de sin(x)
 
La función seno se aproxima con 15 términos de la serie de Taylor:
 
```
sin(x) = x − x³/3! + x⁵/5! − x⁷/7! + ...
```
 
Los signos alternan entre positivo y negativo. Al igual que la exponencial, el programa calcula cada término a partir del anterior para optimizar el proceso. Con 15 términos se obtiene alta precisión para ángulos en el rango habitual.
 
### Coseno — Serie de Taylor de cos(x)
 
Análogo al seno, con 15 términos:
 
```
cos(x) = 1 − x²/2! + x⁴/4! − x⁶/6! + ...
```
 
El primer término es 1 (en lugar de x), y los exponentes del numerador son pares. La misma estrategia de término-a-término se aplica aquí.
 
### Logaritmo natural — Serie de la función artanh
 
Para calcular ln(x), se usa la identidad:
 
```
ln(x) = 2 × arctanh((x−1)/(x+1))
      = 2 × [ u + u³/3 + u⁵/5 + u⁷/7 + ... ]
```
 
donde `u = (x−1)/(x+1)`.
 
Esta serie converge para todo x > 0 y lo hace más rápidamente que la serie clásica `ln(1+x)`. Con 100 términos se obtiene una precisión muy alta. Se valida que x > 0, ya que el logaritmo no está definido para valores negativos o cero.
 
### Seno aproximado en la graficadora
 
Para la función `seno_aprox` en la graficadora, se usa la serie de Taylor truncada a 3 términos:
 
```
seno_aprox(x) = x − x³/6 + x⁵/120
```
 
Esta versión simplificada es suficiente para visualizar la forma de la curva en la consola, donde la resolución es limitada por el tamaño de los caracteres.
