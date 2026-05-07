<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::create('estante_livros', function (Blueprint $table) {
            $table->id();
            $table->foreignId('estante_id')->constrained()->onDelete('cascade');
            $table->foreignId('livro_id')->constrained()->onDelete('cascade');
            $table->boolean('lido')->default(false);
            $table->boolean('is_meta')->default(false);
            $table->integer('ordem')->default(0);
            $table->string('goal_year')->nullable();
            $table->integer('pagina_atual')->default(0);
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('estante_livros');
    }
};
