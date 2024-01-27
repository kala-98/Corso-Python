import pandas as pd 
from fpdf import FPDF

pdf = FPDF(orientation = "portrait", unit = "mm", format = "A4")

df = pd.read_csv("articles.csv")
print(df)

class Article:
    def __init__(self, id_article):
        self.id_article = id_article
        self.name = df.loc[df["id"] == self.id_article, "name"].squeeze()
        self.price = df.loc[df["id"] == self.id_article, "price"].squeeze()

    def available(self):
        try:
            availability = df.loc[df["id"] == self.id_article, ["in stock"]].squeeze()
            if availability > 0:
                return True 
            else:
                return False
            
        except ValueError:
            return False
        
    def buy_article(self):
        availability = df.loc[df["id"] == self.id_article, ["in stock"]].squeeze()
        df.loc[df["id"] == self.id_article, ["in stock"]] = availability - 1
        df.to_csv("articles.csv", index = False)

    def generate(self):
        content = f"""
        Thank your for your reservation!
        Here are your booking data:
        Name: {self.name}
        Price: {self.price}€"""
        return content
    
    def generate_pdf(self):
        pdf.add_page()
        pdf.set_font(family="Times", size=16, style="B")

        pdf.cell(w=50, h=8, txt="Receipt nr.1", ln=1)
        pdf.cell(w=50, h=8, txt=f"Article: {self.name}", ln=1)     
        pdf.cell(w=50, h=8, txt=f"Price: {self.price}", ln=1)
        pdf.output("output/receipt.pdf")

articleId = int(input("Choose the article to buy: "))
article = Article(articleId)

if article.available():
    article.buy_article()
    article.generate_pdf()
    print(article.generate())
else:
    print("Not available")