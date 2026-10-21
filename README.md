# Sort-Study

Resumos de estudo de **Análise e Complexidade de Algoritmos**: recursividade, recorrências e algoritmos de ordenação (Aula 5, Aula 6 e Lista 6), com o cálculo de complexidade passo a passo e os exercícios resolvidos.

| # | Tema | PDF | Markdown |
|---|---|---|---|
| 01 | Recursividade e análise de recorrências (iteração, árvore, substituição, Método Mestre, pilha) | [PDF](Resumos/01_Recursividade_e_Recorrencias.pdf) | [MD](Resumos/01_Recursividade_e_Recorrencias.md) |
| 02 | Ordenação: fundamentos, estabilidade, in-place e comparação | [PDF](Resumos/02_Ordenacao_Fundamentos_e_Comparacao.pdf) | [MD](Resumos/02_Ordenacao_Fundamentos_e_Comparacao.md) |
| 03 | Bubble Sort | [PDF](Resumos/03_Bubble_Sort.pdf) | [MD](Resumos/03_Bubble_Sort.md) |
| 04 | Selection Sort | [PDF](Resumos/04_Selection_Sort.pdf) | [MD](Resumos/04_Selection_Sort.md) |
| 05 | Insertion Sort | [PDF](Resumos/05_Insertion_Sort.pdf) | [MD](Resumos/05_Insertion_Sort.md) |
| 06 | Merge Sort | [PDF](Resumos/06_Merge_Sort.pdf) | [MD](Resumos/06_Merge_Sort.md) |
| 07 | Quick Sort | [PDF](Resumos/07_Quick_Sort.pdf) | [MD](Resumos/07_Quick_Sort.md) |
| 08 | Heap Sort | [PDF](Resumos/08_Heap_Sort.pdf) | [MD](Resumos/08_Heap_Sort.md) |

Onde está cada exercício da Lista 6: 1, 2, 3, 7, 8 e 14 → resumo 02; 4 → 03; 6 → 04; 5 → 05; 9, 10 e 15 → 06; 11 e 12 → 07; 13 → 08. Os "Praticando" 1 a 11 da Aula 5 estão no resumo 01.

Para regerar os PDFs depois de editar os `.md` (requer Microsoft Edge):

```bash
pip install markdown-it-py mdit-py-plugins
python Resumos/build_pdfs.py
```
