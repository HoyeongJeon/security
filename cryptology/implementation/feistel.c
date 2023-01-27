#include <stdint.h>
#include <stdio.h>
#define ROUNDS 8

uint16_t round_f(uint16_t key, uint16_t block);            // round func
uint32_t encrypt(uint16_t L, uint16_t R, uint16_t keys[]); // encrypt func
uint32_t decrypt(uint32_t cipher, uint16_t key[]);         // decrypt func

/*
 key when the size of plaintext is 8byte
  uint32_t keys[ROUNDS] = {0xDEADBEEF, 0xBAADF00D, 0xFEEDFACE, 0xCAFEBABE,
                           0xDEADBABE, 0xD15EA5E,  0xDECEA5ED, 0xBAADAC1D};
*/

int main(void) {
  int secret;
  uint32_t plaintext = 0xD15EA5ED;
  uint16_t keys[ROUNDS] = {0xDEAD, 0xBAAD, 0xFEED, 0xCAFE,
                           0xBEED, 0xD15E, 0xDECE, 0xBAAD};
  uint16_t L = plaintext >> 16;
  uint16_t R = plaintext;
  uint32_t ciphertext = encrypt(L, R, keys);
  uint32_t decrypted_ciphertext = decrypt(ciphertext, keys);
  printf(
      "plaintext is 0x%X\nciphertext is 0x%X\ndecrypted_ciphertext is 0x%X\n",
      plaintext, ciphertext, decrypted_ciphertext);
  return 0;
}

uint16_t round_f(uint16_t block, uint16_t key) { return block ^ key; }

// parameters mean L0 and R0
uint32_t encrypt(uint16_t L, uint16_t R, uint16_t keys[]) {
  uint16_t L_next, R_next, i;
  for (i = 0; i < ROUNDS; i++) {
    L_next = R;
    R_next = round_f(R, keys[i]) ^ L;
    if (i == ROUNDS - 1) // last round
    {
      L = R_next;
      R = L_next;
    } else {
      L = L_next;
      R = R_next;
    }
  }
  return (uint32_t)L << 16 | R;
}

uint32_t decrypt(uint32_t cipher, uint16_t keys[]) {
  uint16_t L = cipher >> 16;
  uint16_t R = cipher;
  uint16_t L_next, R_next, i;
  for (i = 0; i < ROUNDS; i++) {
    L_next = R;
    R_next = L ^ round_f(R, keys[ROUNDS - i - 1]);
    if (i == ROUNDS - 1) // last round
    {
      L = R_next;
      R = L_next;
    } else {
      L = L_next;
      R = R_next;
    }
  }
  return (uint32_t)L << 16 | R;
}
