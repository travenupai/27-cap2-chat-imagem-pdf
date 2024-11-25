from crewai.tools import BaseTool
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
import os

class PDFCreationTool(BaseTool):
    name: str = "PDF Creation Tool"
    description: str = """
    Esta ferramenta gera um arquivo PDF que inclui um título, uma descrição e uma imagem.
    É útil para criar relatórios com elementos visuais incorporados.
    """

    def _run(self, title: str, text: str, image_path: str, output_path: str) -> str:
        """
        Args:
            title (str): O título a ser exibido no PDF.
            text (str): O texto a ser incluído.
            image_path (str): O caminho para a imagem.
            output_path (str): O caminho onde o PDF será salvo.
        Returns:
            str: Nome do arquivo gerado ou mensagem de erro.
        """
        try:
            # Verifica se o arquivo de imagem existe
            if not os.path.exists(image_path):
                return f"Erro: o arquivo de imagem em '{image_path}' não foi encontrado."

            # Criação do PDF usando ReportLab
            c = canvas.Canvas(output_path, pagesize=A4)
            width, height = A4
            margin = 50

            # Adiciona o título ao PDF
            c.setFont("Helvetica-Bold", 16)
            c.drawString(margin, height - 50, title)

            # Adiciona o texto como descrição no PDF
            c.setFont("Helvetica", 12)
            y_position = height - 80

            def draw_wrapped_text(canvas_obj, content, x, y, max_width):
                lines = []
                words = content.split()
                line = []
                for word in words:
                    line.append(word)
                    if canvas_obj.stringWidth(' '.join(line), "Helvetica", 12) > max_width:
                        lines.append(' '.join(line[:-1]))
                        line = [word]
                if line:
                    lines.append(' '.join(line))
                for line in lines:
                    canvas_obj.drawString(x, y, line)
                    y -= 15  # Ajuste para espaçamento entre linhas
                return y

            # Quebra o texto em várias linhas, se necessário
            y_position = draw_wrapped_text(c, text, margin, y_position, width - 2 * margin)

            # Adiciona a imagem no PDF
            try:
                image = ImageReader(image_path)
                c.drawImage(image, 50, height - 350, width=500, height=250, preserveAspectRatio=True)
            except Exception as e:
                return f"Erro ao inserir a imagem no PDF: {e}"

            # Finaliza o PDF
            c.showPage()
            c.save()
            return f"PDF criado com sucesso em '{output_path}'"

        except Exception as e:
            return f"Erro ao criar o PDF: {e}"

