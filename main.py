
import argparse
import json
import unittest
from pathlib import Path

TRILHAS = {
    "python": {
        "nome": "Python",
        "descricao": "Fundamentos, lógica, funções e orientação a objetos.",
        "nivel": "Iniciante ao avançado",
        "modulos": ["Lógica de programação", "Funções", "POO", "Projetos práticos"],
    },
    "sql": {
        "nome": "SQL",
        "descricao": "Consultas, filtros, junções e agregações em bancos de dados.",
        "nivel": "Iniciante ao avançado",
        "modulos": ["SELECT e WHERE", "JOIN", "GROUP BY", "Subconsultas"],
    },
    "engenharia de dados": {
        "nome": "Engenharia de Dados",
        "descricao": "Pipelines, integração e processamento de dados.",
        "nivel": "Intermediário",
        "modulos": ["ETL e ELT", "Modelagem de dados", "Pipelines", "Qualidade de dados"],
    },
}

DESAFIOS = {
    "python": {
        "iniciante": "Crie uma função que receba uma lista de números e retorne a soma.",
        "intermediario": "Crie uma função que conte a frequência de cada palavra em um texto.",
        "avancado": "Implemente um sistema de cache com expiração de resultados.",
    },
    "sql": {
        "iniciante": "Escreva uma consulta que selecione todos os registros de uma tabela.",
        "intermediario": "Escreva uma consulta que agrupe vendas por cliente e calcule o total.",
        "avancado": "Use uma função de janela para classificar vendas por cliente.",
    },
    "engenharia de dados": {
        "iniciante": "Descreva as etapas de um pipeline simples de ingestão de dados.",
        "intermediario": "Projete um pipeline que valide e transforme dados antes de carregá-los.",
        "avancado": "Proponha uma arquitetura de processamento escalável com monitoramento e recuperação de falhas.",
    },
}


def consultar_trilha(tecnologia):
    chave = tecnologia.strip().lower()
    if chave not in TRILHAS:
        raise ValueError(
            f"Trilha não encontrada: {tecnologia}. "
            f"Opções: {', '.join(t['nome'] for t in TRILHAS.values())}"
        )
    return TRILHAS[chave]


def obter_desafio(tecnologia, nivel):
    chave = tecnologia.strip().lower()
    nivel = nivel.strip().lower()

    if chave not in DESAFIOS:
        raise ValueError(f"Tecnologia sem desafios cadastrados: {tecnologia}")

    if nivel not in DESAFIOS[chave]:
        raise ValueError(
            "Nível inválido. Use: iniciante, intermediario ou avancado."
        )

    return DESAFIOS[chave][nivel]


def gerar_certificado(nome, trilha):
    if not nome.strip() or not trilha.strip():
        raise ValueError("Informe o nome da pessoa e o nome da trilha.")

    return (
        "# Certificado de Conclusão\n\n"
        f"Certificamos que **{nome.strip()}** concluiu a trilha "
        f"de aprendizagem **{trilha.strip()}** no projeto Geo-Explorer.\n\n"
        "Este é um certificado demonstrativo, gerado para fins educacionais.\n"
    )


def executar_testes():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestGeoExplorer)
    resultado = unittest.TextTestRunner(verbosity=2).run(suite)
    return resultado.wasSuccessful()


class TestGeoExplorer(unittest.TestCase):
    def test_consultar_python(self):
        self.assertEqual(consultar_trilha("Python")["nome"], "Python")

    def test_trilha_inexistente(self):
        with self.assertRaises(ValueError):
            consultar_trilha("Tecnologia desconhecida")

    def test_desafio_iniciante(self):
        texto = obter_desafio("Python", "iniciante")
        self.assertTrue(len(texto) > 0)

    def test_nivel_invalido(self):
        with self.assertRaises(ValueError):
            obter_desafio("Python", "especialista")

    def test_certificado(self):
        texto = gerar_certificado("Bruna", "Python")
        self.assertIn("Bruna", texto)
        self.assertIn("Python", texto)


def iniciar_mcp():
    try:
        from mcp.server.fastmcp import FastMCP
    except ImportError as exc:
        raise SystemExit(
            "Para usar MCP, instale a dependência: pip install mcp"
        ) from exc

    servidor = FastMCP("Geo-Explorer")

    @servidor.tool()
    def consultar_trilha_aprendizagem(tecnologia: str) -> str:
        """Consulta uma trilha de aprendizagem por tecnologia."""
        return json.dumps(
            consultar_trilha(tecnologia), ensure_ascii=False, indent=2
        )

    @servidor.tool()
    def obter_desafio_programacao(
        tecnologia: str, nivel: str
    ) -> str:
        """Obtém um desafio de programação por tecnologia e nível."""
        return obter_desafio(tecnologia, nivel)

    servidor.run()


def main():
    parser = argparse.ArgumentParser(
        description="Geo-Explorer: trilhas, desafios e certificados."
    )
    subparsers = parser.add_subparsers(dest="comando", required=True)

    trilha_parser = subparsers.add_parser("trilha")
    trilha_parser.add_argument("--tecnologia", required=True)

    desafio_parser = subparsers.add_parser("desafio")
    desafio_parser.add_argument("--tecnologia", required=True)
    desafio_parser.add_argument(
        "--nivel",
        required=True,
        choices=["iniciante", "intermediario", "avancado"],
    )

    certificado_parser = subparsers.add_parser("certificado")
    certificado_parser.add_argument("--nome", required=True)
    certificado_parser.add_argument("--trilha", required=True)

    subparsers.add_parser("testar")
    subparsers.add_parser("mcp")

    args = parser.parse_args()

    try:
        if args.comando == "trilha":
            resultado = consultar_trilha(args.tecnologia)
            print(json.dumps(resultado, ensure_ascii=False, indent=2))

        elif args.comando == "desafio":
            print(obter_desafio(args.tecnologia, args.nivel))

        elif args.comando == "certificado":
            print(gerar_certificado(args.nome, args.trilha))

        elif args.comando == "testar":
            if not executar_testes():
                raise SystemExit(1)

        elif args.comando == "mcp":
            iniciar_mcp()

    except ValueError as erro:
        parser.error(str(erro))


if __name__ == "__main__":
    main()
