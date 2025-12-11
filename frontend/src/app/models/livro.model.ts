import { Autor } from './autor.model';
import { Publisher } from './editora.model';
import { Genero } from './genero.model';
import { Linguagem } from './linguagem.model';

export interface Book {
    id: number;
    nome: string;
    status: boolean;
    autor: Autor;
    publisher: Publisher;
    genero: Genero;
    linguagem: Linguagem;
}
