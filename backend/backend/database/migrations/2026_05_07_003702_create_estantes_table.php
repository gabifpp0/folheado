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
        Schema::create('estantes', function (Blueprint $table) {
            $table->id();
            $table->string('nome');
            $table->foreignId('user_id')->constrained()->onDelete('cascade');
            $table->integer('ordem')->default(0);
            $table->integer('livros_count')->default(0);
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('estantes');
    }
};
