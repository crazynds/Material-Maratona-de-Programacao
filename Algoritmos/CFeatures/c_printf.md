# Printf com nosso amiguinho [Bento](https://github.com/bottle2)

## Detalhes do ```printf()``` e ```scanf()``` no C
Não é discorrido sobre os especificadores de conversão "i", "g", "G", "a", "A", e "p" e os modificadores de comprimento "j" e "t". O tópico de funções de tempo formatado não é abordado. Também não é discutido sobre localização e sua influência no comportamento das funções de string, de tempo e de entrada e saída do C. Codificações multibyte também não são tratados aqui (UTF-8, wchar_t). Leitura de strings com bytes null embutidos, leitura binária e byte order não são explicados, muito menos recuperação e tratamento de erros. É padronizado uma extensão que provê versões “seguras” das funções convencionais, mas não são mostradas.

Funções tipo ```printf()``` e ```scanf()``` usam argumentos variáveis, por isso não há tipagem forte presente. Os tipos informados nas diretivas da string de formato devem casar precisamente com os dos argumentos, ou esses devem ser convertidos explicitamente.
```C
int printf(const char * restrict format, ...);

static char const buffer[2147483648];

int main(void)
{
    printf("%d\n" ,      sizeof buffer); // Wrong interpretaion.
    printf("%d\n" , (int)sizeof buffer); // Cast is not representable.
    printf("%zu\n",      sizeof buffer); // Correct directive.

    return 0;
}
```
As strings de formato do ```printf()``` e ```scanf()``` são parecidas, mas divergem sutilmente em vários aspectos. Em ambos, "%%" se traduz em um "%". Nos demais casos, "%" inicia uma especificação de conversão.

Dos tipos inteiros, é vital informar o modificador de comprimento adequado, que abaixo são demonstrados para a especificação de conversão "d", mas que vale para "u", "o" e "x" também. O sinal do tipo char depende da implementação, uma declaração explícita permite casar corretamente com a diretiva. O tipo unsigned, usado por convenção em operações bitwise, é um unsigned int. Declarações de enum são sempre int, o sinal depende da implementação, mas é forçada a ser signed se uma das enumerações for negativa. O tipo size_t, definido na biblioteca ```<stddef.h>```, usa "%zu" para leitura e impressão. Apesar da impressão em hexadecimal variar com ou sem prefixo e com minúsculas ou maiúsculas, a leitura é sempre com "%x" e derivados. "0x" não é prefixado para o valor zero em diretivas "%#x" e derivadas, se isto é desejado, "0x%x" quebra o galho, idem com maiúsculas.

```C
#include <assert.h>
#include <stdio.h>

int main(void)
{
    FILE *file = tmpfile();

    signed char a = 80;
    short       b = 80;
    int         c = 80;
    long        d = 80;
    long long   e = 80;

    printf(      "%hhd %hd %d %ld %lld\n", a, b, c, d, e);
    fprintf(file, "%hhd %hd %d %ld %lld\n", a, b, c, d, e);

    unsigned int f = 0xABCDEF, f1, f2, f3, f4, f5, f6, f7;
    unsigned     g = 0xABCDEF, g1, g2, g3, g4, g5, g6, g7;

    printf(      "%u %o %#o %x %#x %X %#X\n", f, f, f, f, f, f, f);
    printf(      "%u %o %#o %x %#x %X %#X\n", g, g, g, g, g, g, g);
    fprintf(file, "%u %o %#o %x %#x %X %#X\n", f, f, f, f, f, f, f);
    fprintf(file, "%u %o %#o %x %#x %X %#X\n", g, g, g, g, g, g, g);

    enum { FOO =  5 } h = FOO;
    enum { BAR = -5 } i = BAR;
    size_t            j = sizeof 80;

    printf(      "%u %d %zu\n", h, i, j);
    fprintf(file, "%u %d %zu\n", h, i, j);

    rewind(file);

    fscanf(file, "%hhd %hd %d %ld %lld\n", &a, &b, &c, &d, &e);
    fscanf(file, "%u %o %o %x %x %x %x\n", &f1, &f2, &f3, &f4, &f5, &f6, &f7);
    fscanf(file, "%u %o %o %x %x %x %x\n", &g1, &g2, &g3, &g4, &g5, &g6, &g7);
    fscanf(file, "%u %d %zu\n", &h, &i, &j);

    fclose(file);

    assert(80 == a && 80 == b && 80 == c && 80 == d && 80 == e);
    assert(f == f1 && f == f2 && f == f3 && f == f4 && f == f5 && f == f6 && f == f7);
    assert(g == g1 && g == g2 && g == g3 && g == g4 && g == g5 && g == g6 && g == g7);
    assert(FOO == h && BAR == i && sizeof 80 == j);

    return 0;
}
```
O comprimento dos tipos inteiros do C depende da implementação, isso originou anos de código terrível numa profusão intratável de ```sizeof```, ```#if``` e ```typedef``` que assombram até hoje incontáveis projetos. Como solução, C99 introduziu tipos de tamanho previsível na biblioteca ```<stdint.h>```, e outra biblioteca ```<inttypes.h>``` que define macros para auxiliar na leitura e impressão. Esses tipos devem ser preferidos em todos os casos onde int, unsigned, char e size_t não bastam. Além, é preferível que a leitura seja com "%d", ou se se espera valores muito altos, preferir as diretivas "%" SCNd64 ou "%" SCNu64, para então armazenar na variável de destino somente após checar contra constantes da biblioteca ```<limits.h>``` como SHRT_MAX, ULONG_MIN e outros.

Os macros abstraem o modificador de comprimento e são posicionados após diretivas incompletas "%", e em tempo de pré-processamento se traduzem em literais de strings, concatenadas umas às outras numa única string completa. Para tipos previsíveis sem sinal há, novamente, as variações "u", "o", "x" e "X" em cada macro.

Os tipos definidos variam entre com ou sem sinal, e variam entre tamanho fixo, mínimo ou “rápido”. Tipos “rápidos” podem ser maiores que o especificado, conforme o tipo de endereçamento ou qual tamanho de palavra o processador está otimizado para. Nesse sentido, int tem equilíbrio entre “rapidez” e representatividade. Em arquiteturas sem suporte para tipos mais longos, esses precisam ser emulados: é custoso, mas conveniente.
Importantíssimo: int8_t e uint8_t não usufruem das regras de aliasing do char e unsigned char, ou seja, leitura de arquivos binários e inspeção binária nunca deve ser feita com uint8_t *, sempre com unsigned char * e strings sempre se traduzem em char *, jamais em int8_t *.

```C
#include <assert.h>
#include <inttypes.h>
#include <stdio.h>
#include <stdint.h>

#define PRI_SIGNED_8_16_32_64   "%" PRId8 " %" PRId16 " %"  PRId32 " %"  PRId64
#define PRI_UNSIGNED_8_16_32_64 "%" PRIu8 " %" PRIo16 " %#" PRIx32 " %#" PRIX64
#define PRI_FAST_8_16           "%" PRIdFAST8 " %" PRIuFAST16
#define PRI_LEAST_32_64         "%" PRIdLEAST32 " %" PRIuLEAST64

#define SCN_SIGNED_8_16_32_64   "%" SCNd8 " %" SCNd16 " %" SCNd32 " %" SCNd64
#define SCN_UNSIGNED_8_16_32_64 "%" SCNu8 " %" SCNo16 " %" SCNx32 " %" SCNx64
#define SCN_FAST_8_16           "%" SCNdFAST8 " %" SCNuFAST16
#define SCN_LEAST_32_64         "%" SCNdLEAST32 " %" SCNuLEAST64

int main(void)
{
    FILE *file = tmpfile();

    int8_t  a  = 80;  int16_t b  = 80;  int32_t c  = 80;  int64_t d  = 80;
    uint8_t  au = 80; uint16_t bu = 80; uint32_t cu = 80; uint64_t du = 80;

    int_fast8_t   af  = 80;  int_least32_t cl  = 80;
    uint_fast16_t  bfu = 80; uint_least64_t dlu = 80;

    printf(      PRI_SIGNED_8_16_32_64             "\n", a , b  , c , d  );
    fprintf(file, PRI_SIGNED_8_16_32_64             "\n", a , b  , c , d  );
    printf(      PRI_UNSIGNED_8_16_32_64           "\n", au, bu , cu, du );
    fprintf(file, PRI_UNSIGNED_8_16_32_64           "\n", au, bu , cu, du );
    printf(      PRI_FAST_8_16 " " PRI_LEAST_32_64 "\n", af, bfu, cl, dlu);
    fprintf(file, PRI_FAST_8_16 " " PRI_LEAST_32_64 "\n", af, bfu, cl, dlu);

    rewind(file);

    fscanf(file, SCN_SIGNED_8_16_32_64             "\n", &a , &b  , &c , &d  );
    fscanf(file, SCN_UNSIGNED_8_16_32_64           "\n", &au, &bu , &cu, &du );
    fscanf(file, SCN_FAST_8_16 " " SCN_LEAST_32_64 "\n", &af, &bfu, &cl, &dlu);

    fclose(file);

    assert(80 == a  && 80 == b   && 80 == c  && 80 == d  );
    assert(80 == au && 80 == bu  && 80 == cu && 80 == du );
    assert(80 == af && 80 == bfu && 80 == cl && 80 == dlu);

    return 0;
} 
```
Há três e somente três formas de ler tipos reais. Na impressão, não há especificador de conversão para float.
```C
#include <assert.h>
#include <math.h>
#include <stdio.h>

int main(void)
{
    FILE *file = tmpfile();

    float a = 0.008f; double b = 0.008, b1, b2; long double c = 0.008L;

    double d1 = sqrt(-1.0), d2 = HUGE_VAL, d3 = -HUGE_VAL, d4, d5, d6;

     printf(      "%f %f %Lf %e %E\n", (double)a, b, c, b, b);
    fprintf(file, "%f %f %Lf %e %E\n", (double)a, b, c, b, b);

     printf(      "%f %f %f\n%F %F %F\n", d1, d2, d3, d1, d2, d3);
    fprintf(file, "%f %f %f\n%F %F %F\n", d1, d2, d3, d1, d2, d3);

    rewind(file);

    fscanf(file, "%f %lf %Lf %lf %lf\n", &a, &b, &c, &b1, &b2);
    fscanf(file, "%lf %lf %lf\n%lf %lf %lf\n", &d1, &d2, &d3, &d4, &d5, &d6);

    assert(0.008f == a && 0.008L == c);
    assert(0.008  == b && 0.008  == b1 && 0.008 == b2);
    assert(isnan(d1) && isinf(d2) && isinf(d3));
    assert(isnan(d4) && isinf(d5) && isinf(d6));

    fclose(file);

    return 0;
}
```

As opções de impressão servem para fazer tabelas alinhadinhas. Espaçamento fixo é necessário em vários casos. As flags " " ou "+" ficam bem com alinhamento à esquerda, a não ser que o sinal dos valores seja igual em todas as linhas. Espera-se int, em ordem, para tamanho do campo e precisão, caso usem "*". Interação da flag "#" com especificadores de conversão "g" e "G" difere da com outros para tipos reais. Padding de zeros junto com alinhamento à esquerda, somente possível para inteiros, caso uma precisão seja especificada.
 
```C
#include <stdio.h>

#define INF (1.0 / 0.0)
#define NAN (0.0 / 0.0)

static double const reals[] = {0.0, NAN, 0.08, INF, 8.0, -INF, 8.08, 808.0};
static int    const ints[]  = {-808, -8, 0, 8, 808};
static size_t const n_real  = sizeof reals / sizeof *reals;
static size_t const n_int   = sizeof ints  / sizeof *ints;

#define PRINT_REAL(...) PRINT_LINE(reals, n_real, __VA_ARGS__)
#define PRINT_INT(...)  PRINT_LINE(ints , n_int , __VA_ARGS__)

#define PRINT_LINE(A, N, ...) \
for (unsigned i = 0; i < N; i++) { printf(__VA_ARGS__, A[i]); } putchar('\n');

int main(void)
{
    PRINT_REAL("%11.3f"       );
    PRINT_REAL( "%*.3f", 11   );
    PRINT_REAL( "%*.*f", 11, 3);
    PRINT_REAL("%11.*f",     3);

    PRINT_REAL("%+11.3f");

    PRINT_REAL("  %09.3f" );
    PRINT_REAL("  %+09.3f");

    putchar('\n');

    PRINT_REAL(  "%7.0f"   "    "   );
    PRINT_REAL(  "%7.f"    "    "   );
    PRINT_REAL(  "%7.*f"   "    ", 0);
    PRINT_REAL("  %+05.0f" "    "   );
    PRINT_REAL(  "%+7.0f"  "    "   );

    putchar('\n');

    PRINT_REAL(  "%#8.0f"   "   ");
    PRINT_REAL(  "%+#8.0f"  "   ");
    PRINT_REAL("  %#06.0f"  "   ");
    PRINT_REAL("  %+#06.0f" "   ");
    
    putchar('\n');

    PRINT_INT("%7d"    "    ");
    PRINT_INT("%07d"   "    ");
    PRINT_INT("%+07d"  "    ");
    PRINT_INT("%7.4d"  "    ");
    PRINT_INT("%+7.4d" "    ");

    putchar('\n');

    PRINT_REAL("% -11.3f"    );
    PRINT_REAL("% -*.3f",  11);
    PRINT_REAL("% *.3f" , -11);

    PRINT_REAL("%+-11.3f");
    PRINT_REAL("%+#-11.f");
    PRINT_REAL("% #-11.f");

    putchar('\n');

    PRINT_INT("% -7d"   "    ");
    PRINT_INT("%+-7d"   "    ");
    PRINT_INT("%+-7.5d" "    ");
    PRINT_INT("% -7.5d" "    ");

    return 0;
}
```

A especificação de conversão "s" imprime strings, onde uma precisão limita o quanto é impresso; e "c" recebe um int e imprime um char (literais de caractere como 'k' ou '\a' se traduzem em int e não em char). 

A leitura também usa especificadores de conversão "s" e "c", mas diferindo muito no significado. "s" lê um token composto por caracteres não brancos. "%c" e "%1c" lê um caractere, mais caracteres são lidos arbitrariamente com tamanhos de campo maiores. "[" lê de acordo com um scanset delimitado por um "]" final. ']' é casado se, e somente se ele aparecer no início do scanset. Se '^' aparecer no início do scanset, os caracteres que não aparecem no restante do scanset são casados. O que '-' faz depende da implementação, é comum agir como intervalos de caracteres, e mesmo ASCII não sendo EBCDIC, intervalos como "A-z" reconhecem mais do que somente as letras do alfabeto, de modo que certo cuidado é necessário.

Para esses três especificadores de conversão "s", "c" e "[", uma leitura de zero caracteres é considerada erro. Na leitura, "*" suprime a conversão, ela ocorre, mas não espera ponteiro, nada é gravado e a contagem de conversões não aumenta. Os especificadores de conversão "s" e "[" terminam as strings, porém "c" não adiciona um byte null após a leitura, isto é, o vetor deve ser zerado previamente para constituir uma string legal.

Na leitura, um caractere em branco (' ', '\f', '\n', '\r', '\t' e '\v') na string de formato, qualquer que seja, instrui pular uma sequência de zero ou mais caracteres em branco, quaisquer que sejam. Exemplo: '\t' pulará espaços separando tokens. Em contrapartida, por legibilidade, a diretiva deve ser o que se espera do input, por exemplo: '\n' para fim de linha, ainda que '\f' também o consuma. E sobre fim de linha, '\n' se traduz corretamente na sequência de caracteres de nova linha nativo do sistema (CRLF no Windows, LF no UNIX e CR em sistemas exóticos). Demais caracteres em branco são impressos literalmente. Implicitamente, caracteres em branco são pulados antes de todos especificadores de conversão, exceto "%c" e "%[" (e "%n"), deste modo para esses três últimos, preceder com " " provê o mesmo comportamento.

As partes da string de formato que não espaço em branco ou especificador de conversão leem literalmente o input, e assim que um byte do input difere, para. A função scanf() ou devolve EOF, no caso de fim de input sem nenhuma conversão, ou a quantidade de conversões realizadas: tanto o total esperado, indicando sucesso, ou um número menor, inclusive zero, no caso de falha. Falha esta que pode ser fim de input também, confirmado com outra chamada a scanf() ou feof(stdin). É convenção chamar scanf() dentro de um while e comparar com EOF ou o total esperado de conversões. Se o resultado da leitura for armazenado, deve ser feito entre parênteses, já que atribuição tem a segunda menor precedência. A respeito de leituras propensas a erro, A beginners’ guide away from scanf() é uma ótima referência, que trata também de vulnerabilidades e outras funções de leitura.
 
```C
#include <assert.h>
#include <stdio.h>
#include <string.h>

static char const string[] = "Hello, world!\n\0Secret hello world?\n";

int main(void)
{
    printf("%s", string);
    printf("%.*s\n", (int)strlen(string) - 1, string);
    printf("%.999s", string);
    printf("%.*s\n", 9999, string);

    printf("%.3s%c%c", string, (int)string[3], '!');

    char buffer1[80] = {0};
    char buffer2[80] = {0};
    char buffer3[80] = {0};

    sscanf(string, "%79s%c%c%79s", buffer1, buffer2 + 0, buffer2 + 1, buffer3);
    assert(!strcmp("Hello,", buffer1));
    assert(' ' == buffer2[0]);
    assert('w' == buffer2[1]);
    assert(!strcmp("orld!", buffer3));

    sscanf(string, "%79s %79s", buffer1, buffer2);
    assert(!strcmp("Hello,", buffer1));
    assert(!strcmp("world!", buffer2));

    sscanf(string, "%79c", buffer1);
    assert(!strcmp(string, buffer1));

    memset(buffer1, 0, 80);
    sscanf(string, "%7c", buffer1);
    assert(!strcmp("Hello, ", buffer1));

    assert(1 == sscanf(string, "%*c%79[a-z],%79[a-z]", buffer1, buffer2));
    assert(!strcmp("ello", buffer1));

    sscanf(string, "%79[a-zA-Z], %79[a-z]", buffer1, buffer2);
    assert(!strcmp("Hello", buffer1));
    assert(!strcmp("world", buffer2));

    sscanf(string, "%*[a-zA-Z]%79[, ]", buffer1);
    assert(!strcmp(", ", buffer1));

    sscanf(string, "%79[^,]", buffer1);
    assert(!strcmp("Hello", buffer1));

    sscanf(string, "%79[^\n]", buffer1);
    assert(!strncmp(string, buffer1, strlen(buffer1)));

    sscanf("^-^ emoticons []s!", "%79[]^[a-z !-]", buffer1);
    assert(18 == strlen(buffer1));

    return 0;
}
```
Há outras funções disponíveis. Para impressão literal de string com nova linha automática, há ```puts()```. ```getchar()``` lê um byte por vez, enquanto ```ungetc()``` devolve para a stream até um byte, relido na próxima leitura; alguns sistemas permitem duas, sete, até quinze chamadas sucessivas, no entanto.
