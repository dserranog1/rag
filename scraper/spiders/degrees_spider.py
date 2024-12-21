from pathlib import Path

import scrapy

class DegreesSpider(scrapy.Spider):
    name = "degrees"

    def start_requests(self):
        urls = [
            "https://manizales.unal.edu.co/menu/programas-academicos/carreras/matematicas/"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        sel = scrapy.Selector(response)

        main_content = sel.xpath('//main')
        first_h3 = main_content.xpath('.//h3[1]/text()').get()
        if not first_h3:
            self.log("No H3 found under <main>.")
            return

        first_h3 = first_h3.strip()

        md_content = f"# {first_h3}\n\n"
        processed_h2 = set()  # Track processed H2 elements to avoid duplicates

        tab_container = sel.css(".t3ddy.t3ddy-tabContainer")
        h2_elements = tab_container.css("h2")

        for h2 in h2_elements:
            h2_text = h2.xpath("text()").get()
            if not h2_text or h2_text in processed_h2:
                continue

            processed_h2.add(h2_text.strip())

            md_content += f"## {h2_text.strip()}\n\n"

            parent = h2.xpath("..")

            h3_elements = parent.xpath(".//h3")
            for h3 in h3_elements:
                h3_text = h3.xpath("text()").get()
                if h3_text:
                    md_content += f"### {h3_text.strip()}\n\n"

            h4_elements = parent.xpath(".//h4")
            for h4 in h4_elements:
                h4_text = h4.xpath("text()").get()
                if h4_text:
                    md_content += f"#### {h4_text.strip()}\n\n"

            text_content = parent.xpath(".//text()[normalize-space()]").getall()
            for text in text_content:
                is_strong = parent.xpath(f".//*[text()='{text.strip()}']/ancestor::strong")
                if is_strong:
                    md_content += f"**{text.strip()}**\n\n"
                else:
                    md_content += f"{text.strip()}\n\n"

        file_name = f"{first_h3.replace(' ', '_')}.md"
        output_path = Path(file_name)
        output_path.write_text(md_content, encoding="utf-8")

        self.log(f"Markdown file saved: {output_path}")
