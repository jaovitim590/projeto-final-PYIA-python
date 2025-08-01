CREATE TABLE produtos(
  id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
  nome VARCHAR(255) NOT NULL UNIQUE,
  descricao TEXT NOT NULL,
  quantidade INT NOT NULL CHECK  (quantidade >= 0),
  preco DECIMAL(10,2) NOT NULL CHECK (preco >= 0)
);
CREATE TABLE vendas(
  id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
  id_produto INT NOT NULL,
  quantidade INT NOT NULL CHECK  (quantidade >= 0),
  data_feita DATE NOT NULL,
  FOREIGN KEY (id_produto) REFERENCES produtos(id)
)