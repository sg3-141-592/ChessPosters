import svgutils as sg

fig = sg.transform.SVGFigure("400", "400")

fig1 = sg.transform.fromfile('static/rendered/1/output1.svg')
plot1 = fig1.getroot()
plot1.moveto(25, 25)

txt1 = sg.transform.TextElement(25,425, "1. Kxh2 Qh4+", size=18, weight="normal", font="DejaVuSansMono")

fig.append([plot1, txt1])

fig.save("static/rendered/1/composite.svg")

mainFigure = sg.compose.Figure("210cm", "297cm",
    sg.compose.Panel(
        sg.compose.SVG("static/rendered/1/output1.svg").scale(0.02),
        sg.compose.Text("1. Kxh2 Qh4+", 25, 20, size=12)
    ),
    sg.compose.Panel(
        sg.compose.SVG("static/rendered/1/output2.svg").scale(0.02),
        sg.compose.Text("1. Kxh2 Qh4+", 25, 20, size=12)
    )).tile(3,4)

a = sg.compose.Panel(
    sg.compose.SVG("static/rendered/1/output1.svg"),
    sg.compose.Text("1. Kxh2 Qh4+", 10, 385, size=12)
)
b = sg.compose.Panel(
    sg.compose.SVG("static/rendered/1/output2.svg"),
    sg.compose.Text("1. Kxh2 Qh4+", 10, 385, size=12)
)

c = sg.compose.Figure("800", "400", *[a, b]).tile(2,1)
c.save("static/rendered/1/figure.svg")

# a.save("static/rendered/1/figure.svg")

# mainFigure.save("static/rendered/1/figure.svg")
