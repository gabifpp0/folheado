import { Author } from './author.model';
import { Publisher } from './publisher.model';
import { Genre } from './genre.model';
import { Language } from './language.model';

export interface Book {
    id: number;
    name: string;
    status: boolean;
    author: Author;
    publisher: Publisher;
    genre: Genre;
    language: Language;
}
