from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak
)

from reportlab.lib.styles import (
    getSampleStyleSheet,
    ParagraphStyle
)

from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors
from reportlab.lib.units import cm
import os


# ============================================================
# ARQUIVO DE SAÍDA
# ============================================================

path = "/mnt/data/Mapa_Pegada_Digital_Aridio_Silva_Atualizado_Bibliografia.pdf"


# ============================================================
# ESTILOS
# ============================================================

styles = getSampleStyleSheet()

styles.add(
    ParagraphStyle(
        name="TitleX",
        parent=styles["Title"],
        fontSize=23,
        leading=28,
        alignment=TA_CENTER,
        fontName="Helvetica-Bold"
    )
)

styles.add(
    ParagraphStyle(
        name="SubX",
        parent=styles["Normal"],
        fontSize=10.5,
        leading=14,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#555555")
    )
)

styles.add(
    ParagraphStyle(
        name="H1X",
        parent=styles["Heading1"],
        fontSize=15,
        leading=19,
        fontName="Helvetica-Bold",
        spaceBefore=10,
        spaceAfter=7
    )
)

styles.add(
    ParagraphStyle(
        name="BodyX",
        parent=styles["BodyText"],
        fontSize=9.8,
        leading=13.5,
        spaceAfter=7
    )
)

styles.add(
    ParagraphStyle(
        name="RefX",
        parent=styles["BodyText"],
        fontSize=8.2,
        leading=10.5,
        textColor=colors.HexColor("#444444"),
        leftIndent=8
    )
)


# ============================================================
# DOCUMENTO
# ============================================================

doc = SimpleDocTemplate(
    path,
    pagesize=A4,
    leftMargin=1.55 * cm,
    rightMargin=1.55 * cm,
    topMargin=1.4 * cm,
    bottomMargin=1.4 * cm
)

S = []


# ============================================================
# CAPA
# ============================================================

S += [

    Spacer(1, 1 * cm),

    Paragraph(
        "MAPA DA PEGADA DIGITAL",
        styles["TitleX"]
    ),

    Paragraph(
        "ARIDIO SILVA",
        styles["TitleX"]
    ),

    Spacer(1, .3 * cm),

    Paragraph(
        "Relatório atualizado com Bibliografia e Evidências de Citação",
        styles["SubX"]
    ),

    Paragraph(
        "23 de agosto de 2026",
        styles["SubX"]
    ),

    Spacer(1, .8 * cm),

    Paragraph(
        "Resumo executivo",
        styles["H1X"]
    ),

    Paragraph(
        """
        A atualização amplia o mapa anterior com uma seção dedicada à
        produção editorial de Arídio/Aridio Silva e às evidências públicas
        de uso, referência e citação das obras.

        Foram priorizadas fontes institucionais, acadêmicas, jurídicas e
        bibliográficas. Quando uma obra é confirmada, mas a contagem
        específica no Google Acadêmico não pôde ser verificada diretamente,
        o relatório não inventa um número de citações.
        """,
        styles["BodyX"]
    )
]


# ============================================================
# MAPA DA PRESENÇA DIGITAL
# ============================================================

S.append(
    Paragraph(
        "1. MAPA DA PRESENÇA DIGITAL",
        styles["H1X"]
    )
)

data = [

    [
        "Núcleo",
        "Superfícies",
        "Evidência"
    ],

    [
        "Identidade profissional",
        "Perfil profissional e conteúdo técnico",
        "Carreira sênior em software e tecnologia"
    ],

    [
        "Produção editorial",
        "Livros publicados",
        "Quatro títulos confirmados com diferentes níveis de evidência"
    ],

    [
        "Impacto acadêmico/institucional",
        "Universidades, periódicos e documentos públicos",
        "Obras usadas em bibliografias e referências"
    ],

    [
        "Código e conhecimento",
        "GitHub e projetos públicos",
        "Padrões, TDD, IA/ML e blockchain"
    ],

    [
        "Conteúdo contemporâneo",
        "Artigos e comunidades",
        "IA generativa e engenharia de software"
    ]
]


t = Table(
    data,
    colWidths=[
        4.1 * cm,
        6.2 * cm,
        7.0 * cm
    ],
    repeatRows=1
)


t.setStyle(

    TableStyle([

        (
            "BACKGROUND",
            (0, 0),
            (-1, 0),
            colors.HexColor("#203864")
        ),

        (
            "TEXTCOLOR",
            (0, 0),
            (-1, 0),
            colors.white
        ),

        (
            "FONTNAME",
            (0, 0),
            (-1, 0),
            "Helvetica-Bold"
        ),

        (
            "GRID",
            (0, 0),
            (-1, -1),
            .35,
            colors.HexColor("#B8C4D6")
        ),

        (
            "ROWBACKGROUNDS",
            (0, 1),
            (-1, -1),
            [
                colors.white,
                colors.HexColor("#EEF3F8")
            ]
        ),

        (
            "VALIGN",
            (0, 0),
            (-1, -1),
            "TOP"
        ),

        (
            "FONTSIZE",
            (0, 0),
            (-1, -1),
            8.3
        ),

        (
            "TOPPADDING",
            (0, 0),
            (-1, -1),
            6
        ),

        (
            "BOTTOMPADDING",
            (0, 0),
            (-1, -1),
            6
        )

    ])

)

S.append(t)

S.append(
    PageBreak()
)


# ============================================================
# BIBLIOGRAFIA
# ============================================================

S.append(
    Paragraph(
        "2. BIBLIOGRAFIA PUBLICADA IDENTIFICADA",
        styles["H1X"]
    )
)


books = [

    (

        "<b>Bug do Milênio — Antes, Durante e Depois</b>",

        """
        1999, Revan, 320 páginas, ISBN 857106190-4.

        A autoria e os dados bibliográficos aparecem no perfil profissional
        público associado a Aridio Silva e são reforçados pela descrição
        editorial posterior da Revan.
        """

    ),

    (

        "<b>Dominando a Tecnologia de Objetos — "
        "Programação, Implementação, Soluções, Problemas: "
        "UML/Java/C++</b>",

        """
        Book Express, 2002.

        A referência bibliográfica foi localizada em documento da UDESC
        como bibliografia de disciplina de orientação a objetos, confirmando
        título, autoria, editora e ano.
        """

    ),

    (

        "<b>Desvendando o Pregão Eletrônico</b>",

        """
        Revan, 2002, em coautoria com J. Araújo Ribeiro e
        Luis A. Rodrigues.

        A obra é identificada em registros editoriais e em múltiplas
        citações acadêmicas e jurídicas.
        """

    ),

    (

        "<b>Sistemas de Informação na Administração Pública</b>",

        """
        Revan, 2004, em coautoria com José Araújo Ribeiro e
        Luis Rodrigues.

        A obra permanece presente em bibliografias universitárias e
        artigos acadêmicos.
        """

    )

]


for title, description in books:

    S.append(
        Paragraph(
            title,
            styles["H1X"]
        )
    )

    S.append(
        Paragraph(
            description,
            styles["BodyX"]
        )
    )


# ============================================================
# CITAÇÕES E USO ACADÊMICO
# ============================================================

S.append(
    Paragraph(
        "3. EVIDÊNCIAS DE CITAÇÃO E USO ACADÊMICO/INSTITUCIONAL",
        styles["H1X"]
    )
)


evid = [

    (

        "<b>Desvendando o Pregão Eletrônico</b>",

        """
        Há evidência direta de uso da obra como referência em pesquisa
        jurídica publicada em 2023, em documento do Tribunal de Contas
        e em análises sobre licitações.

        Um documento reproduz e atribui uma definição da obra à página 34.
        Outro trabalho jurídico referencia páginas 142 e 177.

        Isso demonstra uso tanto bibliográfico quanto textual.
        """

    ),

    (

        "<b>Sistemas de Informação na Administração Pública</b>",

        """
        A obra aparece como referência em artigo da Revista de Administração
        Pública hospedado na SciELO, em programa/bibliografia de disciplina
        da UNESP e em artigo do Informe Econômico da UFPI.

        Essas ocorrências demonstram circulação acadêmica e uso como
        literatura de apoio.
        """

    ),

    (

        "<b>Dominando a Tecnologia de Objetos</b>",

        """
        Foi localizado como item da bibliografia principal de disciplina
        da UDESC.

        A referência registra:

        SILVA, Aridio. Dominando a tecnologia de objetos –
        programação, implementação, soluções, problemas:
        UML/JAVA/C++.

        Rio de Janeiro: Book Express, 2002.
        """

    ),

    (

        "<b>Bug do Milênio — Antes, Durante e Depois</b>",

        """
        A autoria e os dados bibliográficos estão confirmados por fonte
        profissional e pela apresentação editorial posterior.

        Nesta atualização não foi localizada uma evidência acadêmica forte
        de citação específica; portanto, o impacto acadêmico permanece
        como não quantificado.
        """

    )

]


for title, description in evid:

    S.append(
        Paragraph(
            title,
            styles["H1X"]
        )
    )

    S.append(
        Paragraph(
            description,
            styles["BodyX"]
        )
    )


# ============================================================
# NOVA PÁGINA
# ============================================================

S.append(
    PageBreak()
)


# ============================================================
# REFERÊNCIAS
# ============================================================

S.append(
    Paragraph(
        "4. REFERÊNCIAS E CITAÇÕES ENCONTRADAS",
        styles["H1X"]
    )
)


refs = [

    (

        "<b>Fonte 1 — LinkedIn / perfil de Aridio Silva.</b>",

        """
        Confirma Bug do Milênio — Antes, Durante e Depois,
        Revan, 1999, 320 páginas, ISBN 857106190-4.
        """

    ),

    (

        "<b>Fonte 2 — UDESC, bibliografia de disciplina.</b>",

        """
        Registra:

        SILVA, Aridio. Dominando a tecnologia de objetos –
        programação, implementação, soluções, problemas:
        UML/JAVA/C++.

        Rio de Janeiro: Book Express, 2002.
        """

    ),

    (

        "<b>Fonte 3 — Journal of Law and Sustainable Development, 2023.</b>",

        """
        Lista SILVA, Arídio; RIBEIRO, José Araújo;
        RODRIGUES, Luiz Alberto.

        Desvendando o Pregão Eletrônico.
        Revan, 2002.

        como referência.
        """

    ),

    (

        "<b>Fonte 4 — Documento institucional/jurisprudencial do TCU.</b>",

        """
        Atribui a Arídio Silva, em Desvendando o Pregão Eletrônico,
        p. 34, uma formulação usada na discussão sobre bens e
        serviços comuns.
        """

    ),

    (

        "<b>Fonte 5 — Âmbito Jurídico.</b>",

        """
        Referencia Desvendando o Pregão Eletrônico, Revan, 2002,
        incluindo citações às páginas 142 e 177.
        """

    ),

    (

        "<b>Fonte 6 — SciELO / Revista de Administração Pública.</b>",

        """
        Inclui Sistemas de Informação na Administração Pública,
        Revan, 2004, na bibliografia de artigo acadêmico.
        """

    ),

    (

        "<b>Fonte 7 — UNESP.</b>",

        """
        Inclui Sistemas de Informação na Administração Pública
        na bibliografia de disciplina de Tecnologia da Informação
        na Administração Pública.
        """

    ),

    (

        "<b>Fonte 8 — Informe Econômico / UFPI.</b>",

        """
        Inclui Sistemas de Informação na Administração Pública
        em referências bibliográficas de artigo acadêmico.
        """

    ),

    (

        "<b>Fonte 9 — Editora Revan / catálogo editorial.</b>",

        """
        Apresenta Sistemas de Informação na Administração Pública
        e registra Arídio como autor também de Bug do Milênio e
        Desvendando o Pregão Eletrônico.
        """

    )

]


for source, description in refs:

    S.append(
        Paragraph(
            source,
            styles["RefX"]
        )
    )

    S.append(
        Paragraph(
            description,
            styles["RefX"]
        )
    )

    S.append(
        Spacer(1, 3)
    )


# ============================================================
# GOOGLE ACADÊMICO
# ============================================================

S.append(
    Paragraph(
        "5. NOTA SOBRE GOOGLE ACADÊMICO",
        styles["H1X"]
    )
)


S.append(
    Paragraph(
        """
        As evidências acima demonstram que as obras aparecem em documentos
        e publicações acadêmicas indexáveis e, em vários casos, em fontes
        tipicamente recuperadas por mecanismos acadêmicos.

        Entretanto, este relatório não atribui uma contagem numérica de
        citações do Google Acadêmico sem acesso verificável à página de
        resultados ou ao perfil correspondente.

        Assim, a formulação correta é:

        <b>existem citações e referências acadêmicas públicas verificáveis</b>;

        a contagem consolidada no Google Acadêmico permanece uma etapa
        específica de auditoria bibliométrica.
        """,
        styles["BodyX"]
    )
)


# ============================================================
# CONCLUSÃO
# ============================================================

S.append(
    Paragraph(
        "6. CONCLUSÃO ATUALIZADA",
        styles["H1X"]
    )
)


S.append(
    Paragraph(
        """
        A produção editorial identificada reforça significativamente a
        pegada digital: ela começa antes da popularização das redes sociais,
        atravessa governo eletrônico e orientação a objetos e permanece
        recuperável em fontes acadêmicas, institucionais e profissionais.

        O ativo mais forte em termos de evidência de uso acadêmico e
        institucional é atualmente o conjunto formado por
        <i>Desvendando o Pregão Eletrônico</i> e
        <i>Sistemas de Informação na Administração Pública</i>,
        enquanto <i>Dominando a Tecnologia de Objetos</i> possui
        confirmação de adoção em bibliografia universitária.
        """,
        styles["BodyX"]
    )
)


S.append(
    Spacer(1, .5 * cm)
)


S.append(
    Paragraph(
        """
        Relatório atualizado em 23 de agosto de 2026.

        Fontes consultadas: LinkedIn, UDESC,
        Journal of Law and Sustainable Development,
        documentos institucionais do TCU,
        Âmbito Jurídico, SciELO, UNESP, UFPI
        e catálogo editorial da Revan.
        """,
        styles["RefX"]
    )
)


# ============================================================
# GERAÇÃO DO PDF
# ============================================================

doc.build(S)


print(
    "PDF gerado com sucesso:"
)

print(path)

print(
    "Tamanho:",
    os.path.getsize(path),
    "bytes"
)