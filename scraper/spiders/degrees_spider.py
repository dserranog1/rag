from pathlib import Path

import scrapy


class DegreesSpider(scrapy.Spider):
    name = "degrees"

    def start_requests(self):
        urls = [
            # undergrad
            "https://manizales.unal.edu.co/menu/programas-academicos/carreras/matematicas/",
            "https://manizales.unal.edu.co/menu/programas-academicos/carreras/administracion-de-empresas/",
            "https://www.manizales.unal.edu.co/menu/programas-academicos/carreras/administracion-de-sistemas-informaticos/",
            "https://www.manizales.unal.edu.co/menu/programas-academicos/carreras/arquitectura/",
            "https://www.manizales.unal.edu.co/menu/programas-academicos/carreras/gestion-cultural-y-comunicativa/",
            "https://www.manizales.unal.edu.co/menu/programas-academicos/carreras/ingenieria-civil/",
            "https://www.manizales.unal.edu.co/menu/programas-academicos/carreras/ingenieria-electrica/",
            "https://www.manizales.unal.edu.co/menu/programas-academicos/carreras/ingenieria-electronica/",
            "https://www.manizales.unal.edu.co/menu/programas-academicos/carreras/ingenieria-fisica/",
            "https://www.manizales.unal.edu.co/menu/programas-academicos/carreras/ingenieria-industrial/",
            "https://www.manizales.unal.edu.co/menu/programas-academicos/carreras/ingenieria-quimica/",
            # grad
            # "http://www.fadmon.unal.edu.co/inicio/formacion/posgrados/especializacion-en-gestion-de-redes-de-datos.html", page is down
            # "http://www.fadmon.unal.edu.co/inicio/formacion/posgrados/especializacion-en-bionegocios.html", page is down
            # "http://www.fadmon.unal.edu.co/inicio/formacion/posgrados/especializacion-en-alta-gerencia.html", page is down
            # "http://www.fadmon.unal.edu.co/inicio/formacion/posgrados/especializacion-en-auditoria-de-sistemas.html", page is down
            "https://www.manizales.unal.edu.co/menu/programas-academicos/posgrados/especializacion-en-direccion-de-produccion-y-operaciones/",
            # "http://www.fadmon.unal.edu.co/inicio/formacion/posgrados/especializacion-en-finanzas-corporativas.html", page is down
            # "http://www.fadmon.unal.edu.co/inicio/formacion/posgrados/especializacion-en-gerencia-estrategica-de-proyectos.html", page is down
            # "http://www.fadmon.unal.edu.co/inicio/formacion/posgrados/especializacion-en-gestion-cultural.html", page is down
            "https://www.manizales.unal.edu.co/menu/programas-academicos/posgrados/especializacion-en-ingenieria-ambiental-area-sanitaria/",
            # "http://www.fia.unal.edu.co/index.php?option=com_content&view=article&id=263&Itemid=151", page is down
            # "http://www.fia.unal.edu.co/index.php?option=com_content&view=article&id=264&Itemid=151", page is down
            # "http://www.fia.unal.edu.co/index.php?option=com_content&view=article&id=535&Itemid=151", page is down
            "https://www.manizales.unal.edu.co/menu/programas-academicos/posgrados/maestria-de-profundizacion-en-ingenieria-industrial/",
            # "http://www.fadmon.unal.edu.co/inicio/formacion/posgrados/maestria-en-administracion-de-sistemas-informaticos-investigacion.html", page is down
            # "http://www.fadmon.unal.edu.co/inicio/formacion/posgrados/maestria-en-administracion-de-sistemas-informaticos-profundizacion.html", page down
            # "http://www.fadmon.unal.edu.co/inicio/formacion/posgrados/maestria-en-administracion-investigacion.html", page is down
            # "http://www.fadmon.unal.edu.co/inicio/formacion/posgrados/maestria-en-administracion-profundizacion.html", page is down
            "https://www.manizales.unal.edu.co/menu/programas-academicos/posgrados/maestria-en-arquitectura/",
            "https://www.manizales.unal.edu.co/menu/programas-academicos/posgrados/maestria-en-ciencias-fisica/",
            "https://www.manizales.unal.edu.co/menu/programas-academicos/posgrados/maestria-en-ciencias-matematica-aplicada/",
            "https://www.manizales.unal.edu.co/menu/programas-academicos/posgrados/maestria-en-ensenanza-de-las-ciencias-exactas-y-naturales/",
            # "http://www.fadmon.unal.edu.co/inicio/formacion/posgrados/maestria-en-gestion-cultural-investigacion.html", page is down
            # "http://www.fadmon.unal.edu.co/inicio/formacion/posgrados/maestria-en-gestion-cultural-investigacion.html", page is down
            "https://www.manizales.unal.edu.co/menu/programas-academicos/posgrados/maestria-en-habitat/",
            "https://www.manizales.unal.edu.co/menu/programas-academicos/posgrados/maestria-en-ingenieria-automatizacion-industrial/",
            # "http://www.fia.unal.edu.co/index.php?option=com_content&view=article&id=276&Itemid=152", page is down
            # "http://www.fia.unal.edu.co/index.php?option=com_content&view=article&id=275&Itemid=152", page is down
            "https://www.manizales.unal.edu.co/menu/programas-academicos/posgrados/maestria-en-ingenieria-ingenieria-ambiental/",
            "https://www.manizales.unal.edu.co/menu/programas-academicos/posgrados/maestria-en-ingenieria-ingenieria-electrica/",
            "https://www.manizales.unal.edu.co/menu/programas-academicos/posgrados/maestria-en-ingenieria-ingenieria-quimica/",
            # "http://www.fia.unal.edu.co/index.php?option=com_content&view=article&id=306&Itemid=152", page is down
            "https://www.manizales.unal.edu.co/menu/programas-academicos/posgrados/maestria-en-medio-ambiente-y-desarrollo/",
            "https://www.manizales.unal.edu.co/menu/programas-academicos/posgrados/maestria-investigativa-en-ingenieria-industrial/",
            # "http://www.fadmon.unal.edu.co/inicio/formacion/posgrados/doctorado-en-administracion.html", page is down
            "https://www.manizales.unal.edu.co/menu/programas-academicos/posgrados/doctorado-en-ingenieria-industria-y-organizaciones/",
            "https://www.manizales.unal.edu.co/menu/programas-academicos/posgrados/doctorado-en-ingenieria-linea-de-investigacion-en-automatica/",
            "https://www.manizales.unal.edu.co/menu/programas-academicos/posgrados/doctorado-en-ingenieria-ingenieria-quimica/",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        sel = scrapy.Selector(response)

        main_content = sel.xpath("//main")
        first_h3 = main_content.xpath(".//h3[1]/text()").get()
        if not first_h3:
            self.log("No H3 found under <main>.")
            return

        first_h3 = first_h3.strip()

        # Extract metadata
        # page_title = response.xpath("//title/text()").get().strip()
        url = response.url
        # extracted_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        md_content = f"---\n"
        md_content += f"url: {url}\n"
        # md_content += f"extracted: {extracted_date}\n"
        md_content += f"---\n\n"

        md_content += f"# {first_h3}\n\n"

        # Find all elements with the class "t3ddy-item t3ddy-tab-item"
        tab_items = sel.css(".t3ddy-item.t3ddy-tab-item")

        for tab_item in tab_items:
            # Extract all text content within the tab item
            text_content = tab_item.xpath(".//text()[normalize-space()]").getall()
            for text in text_content:
                md_content += f"{text.strip()}\n\n"

        # Save the markdown content to a file in the "documents" folder
        output_dir = Path("documents")
        output_dir.mkdir(exist_ok=True)
        file_name = f"{first_h3.replace(' ', '_')}.md"
        output_path = output_dir / file_name
        output_path.write_text(md_content, encoding="utf-8")

        self.log(f"Markdown file saved: {output_path}")
