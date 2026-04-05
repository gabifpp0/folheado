CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL, 
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  
);

CREATE TABLE livros (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    autor VARCHAR(255) NOT NULL,
    descricao TEXT,
    pagina INT NOT NULL,
    capa TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE estantes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    user_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_estante_user 
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,

    CONSTRAINT unique_user_estante 
        UNIQUE (user_id, nome)
);

CREATE TABLE estante_livros (
    id SERIAL PRIMARY KEY,
    estante_id INT NOT NULL,
    livro_id INT NOT NULL,
    is_meta BOOLEAN DEFAULT FALSE,
    goal_year INT,
    current_page INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_estante 
        FOREIGN KEY (estante_id) REFERENCES estantes(id) ON DELETE CASCADE,

    CONSTRAINT fk_livro 
        FOREIGN KEY (livro_id) REFERENCES livros(id) ON DELETE CASCADE,

    CONSTRAINT unique_estante_livro 
        UNIQUE (estante_id, livro_id)
);

CREATE TABLE avaliacoes (
    id SERIAL PRIMARY KEY,
    livro_id INT NOT NULL,
    user_id INT NOT NULL,
    nota INT CHECK (nota >= 1 AND nota <= 5),
    comentario TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_avaliacao_livro 
        FOREIGN KEY (livro_id) REFERENCES livros(id) ON DELETE CASCADE,

    CONSTRAINT fk_avaliacao_user 
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,

    CONSTRAINT unique_user_livro_avaliacao 
        UNIQUE (user_id, livro_id)
);