function ExibirGraficoNotas()
    a = load('Alunos.mat');
    bar(a.notas);
    grid on;
    xlabel('Alunos');
    ylabel('Notas');    
end