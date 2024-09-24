#include<stdio.h>
#include<stdlib.h>
#include<time.h>
// parameter from MRGK32a 
#define norm 2.328306549295728e-10
#define m1   4294967087.0
#define m2   4294944443.0
#define a12     1403580.0
#define a13n     810728.0
#define a21      527612.0
#define a23n    1370589.0

/***
The seeds for s10, s11, s12 must be integers in [0, m1 - 1] and not all 0. 
The seeds for s20, s21, s22 must be integers in [0, m2 - 1] and not all 0. 
***/

int main(){
   time_t y ;
   y = time(NULL);
   //printf("%ld\n", y);
   double SEED = y;
   //printf("%ld", y);
   double s10 = SEED, s11 = SEED, s12 = SEED, s20 = SEED, s21 = SEED, s22 = SEED;

   for (int i=0;i<1000000;i++){
      long k;
      double p1, p2;
      /* Component 1 */
      p1 = a12 * s11 - a13n * s10;
      k = p1 / m1;
      p1 -= k * m1;
      if (p1 < 0.0)
         p1 += m1;
      s10 = s11;
      s11 = s12;
      s12 = p1;

      /* Component 2 */
      p2 = a21 * s22 - a23n * s20;
      k = p2 / m2;
      p2 -= k * m2;
      if (p2 < 0.0)
         p2 += m2;
      s20 = s21;
      s21 = s22;
      s22 = p2;

      /* Combination */
      if (p1 <= p2)
         printf("%lf ",((p1 - p2 + m1) * norm)) ;
      else
         printf("%lf ",((p1 - p2) * norm)) ;
      }

   return 0;
}