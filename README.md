# Restaurante Chapa Quente - Ferramenta de Construção de Cardápios

Bem-vindo ao projeto de construção de cardápios para o Restaurante Chapa Quente! Este projeto foi desenvolvido como parte do módulo de Ciência da Computação na `Trybe`, utilizando a linguagem Python.

## Descrição do Projeto
O Restaurante 🍝 🦐 Chapa Quente 🍛 🥘 precisa de uma ferramenta eficiente para gerar cardápios levando em consideração restrições alimentares e disponibilidade de ingredientes em estoque. Atualmente, a gestão de receitas e estoque é ineficiente, utilizando arquivos CSV. Neste projeto, você será responsável por construir testes, implementar classes e melhorar a gestão do restaurante.

## Habilidades Exercitadas
- Prática do conceito de Hashmaps com estruturas de dados Dict e Set em Python.
- Aplicação de conhecimentos em testes de software.
- Exercício de conhecimentos em orientação a objetos.

## Desafios
### 1 - Testando classes já implementadas parte 1
Implemente testes para a classe Ingredient localizada em `src/models/ingredient.py`. Os testes devem garantir que a classe pode ser instanciada corretamente, o atributo restrictions é populado corretamente, e os métodos mágicos funcionam conforme esperado.

### 2 - Testando classes já implementadas parte 2
Implemente testes para a classe Dish localizada em `src/models/dish.py`. Os testes devem garantir a correta instanciação da classe, o correto funcionamento dos métodos mágicos, e a validação adequada ao criar pratos inválidos.

### 3 - Mapeamento Pratos <> Ingredientes
Implemente a classe MenuData em `src/services/menu_data.py`. Esta classe realizará o mapeamento de pratos e ingredientes com base em um arquivo CSV fornecido. Garanta que a classe seja capaz de ler o arquivo CSV, instanciar pratos e ingredientes, e conter um atributo `dishes` com todos os pratos devidamente instanciados.

### 4 - Geração dos Cardápios
Implemente o método `get_main_menu` na classe MenuBuilder localizada em `src/services/menu_builder.py`. Este método deve gerar o cardápio com base nas restrições alimentares e disponibilidade de ingredientes em estoque. A classe deve ser instanciada corretamente, e o método deve retornar uma lista de dicionários representando o cardápio.

### 5 - Estoque de Ingredientes
Complete a implementação da classe InventoryMapping em `src/services/inventory_control.py`. Implemente os métodos `check_recipe_availability` e `consume_recipe`, que verificam a disponibilidade de ingredientes em estoque e consomem os ingredientes da receita, respectivamente.

### 6 - Cardápios baseados no Estoque
Aprimore o método `get_main_menu` para considerar a disponibilidade em estoque dos ingredientes dos pratos. Utilize a classe InventoryMapping para acessar as informações do estoque. Certifique-se de que o método retorna corretamente uma lista vazia quando o estoque não possui os ingredientes necessários.

# Como Executar a Aplicação
Para ver a aplicação rodando com as funcionalidades implementadas, utilize o seguinte comando:

```bash
python3 -m uvicorn app:app
```

Acesse a rota `/docs` para visualizar a documentação gerada pelo FastAPI.📚🚀
