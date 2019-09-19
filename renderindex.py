import pandas as pd

def extractor(filename):
    source = pd.read_csv(filename)
    sort_source = source.sort_values("Date", ascending=False)
    num_rows, _ = sort_source.shape

    data = []
    for index, row in sort_source.iterrows():
        data.append([row['Link'], row['Title'], row['Date'], row['Author'], row['Description']])

    return data

def html_generator(data):
    HTML = '''<!DOCTYPE HTML>
<!--
	Binary by TEMPLATED
	templated.co @templatedco
	Released for free under the Creative Commons Attribution 3.0 license (templated.co/license)
-->
<html>

<head>
	<title>Opening Data</title>
	<meta charset="utf-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1" />
	<link rel="stylesheet" href="assets/css/main.css" />
	<!-- <link rel="icon" href="./assets/images/icon.png" /> favicon goes here -->

</head>

<body>

	<!-- Header -->
	<header id="header" style="background-color: rgb(252,252,252);">
		<a href="index.html" class="logo" style="color: #1c1c1c;"><strong>Opening Data</strong> - Making Open Data Accessible</a>
	</header>


	<!-- Banner -->
	<section id="banner" style="background-color: rgb(252,252,252);">
		<div class="inner">
			<h1 style="color: #1c1c1c;">Opening Data</h1>
			<ul class="actions" style="color: #1c1c1c;">
				<li><a href="about.html" class="button alt scrolly big" style="color: #1c1c1c;text-decoration:underline">About</a></li>
				<li><a href="https://openingdata.github.io/single-issuer-districts/" class="button alt scrolly big" style="color: #1c1c1c;text-decoration:underline">Most Recent Blog</a></li>
				<li><a href="community_guidelines.html" class="button alt scrolly big" style="color: #1c1c1c;text-decoration:underline">Community Guidelines</a></li>
			</ul>

		</div>
	</section>
'''
    template_1 = '''
		<div class="content" style="background-color: #1c1c1c; color: #fcfcfc;">
			<div class="inner">
				<header>
					<h2><a href="{}" style="color: #fcfcfc;">{}</a></h2>
					<p class="info" style="border-color: rgba(255, 255, 255, 0.5); color: rgba(255, 255, 255, 0.5);">{}<a href="#" style="color:#fff"> {}</a></p>
				</header>
				<p style="color: #fcfcfc;">{}</p>

			</div>
		</div>
        '''
    template_2 = '''
		<div class="content" style="background-color: #fcfcfc; color=rgba(255, 255, 255, 0.75);">
			<div class="inner">
				<header>
					<h2><a href="{}" style="color: #1c1c1c;">{}</a></h2>
					<p class="info" style="border-color: #1c1c1c; color: #1c1c1c;">{}<a href="#" style="color: #1c1c1c;"> {}</a></p>
				</header>
				<p style="color:#1c1c1c;">{}</p>

			</div>
		</div>
    '''

    switch = False
    for i in range(0, len(data), 2):
        if i + 1 < len(data):
            HTML += '<article id="one" class="post style1">'

            d1 = data[i]
            d2 = data[i+1]

            odate1 = str(d1[2])
            odate2 = str(d2[2])
            d1date = odate1[4:6]+'/'+odate1[6:]+'/'+odate1[:4]
            d2date = odate2[4:6]+'/'+odate2[6:]+'/'+odate2[:4]

            side_1 = template_1.format(d1[0], d1[1], d1date, d1[3], d1[4] )
            side_2 = template_2.format(d2[0], d2[1], d2date, d2[3], d2[4] )

            if switch:
                HTML += side_2
                HTML+= side_1
            else:
                HTML+= side_1
                HTML += side_2
            HTML += '</article>'
        else: 
            HTML += '<article id="one" class="post style1">'

            d1 = data[i]
            odate1 = str(d1[2])
            d1date = odate1[4:6]+'/'+odate1[6:]+'/'+odate1[:4]

            side_1 = template_1.format(d1[0], d1[1], d1date, d1[3], d1[4] )
            side_2 = template_2.format('#', 'At the end', 'NA/Na/Na', 'NA', 'Please contribute a story!')


            if switch:
                HTML += side_2
                HTML+= side_1
            else:
                HTML+= side_1
                HTML += side_2
            HTML += '</article>'

        switch = not switch 
    HTML += '''
	<footer id="footer">

		<div class="copyright">
			Original Design: <a href="https://templated.co">TEMPLATED</a>, modified by OpeningData
		</div>
	</footer>

</body>

</html>'''

    return HTML

def main():
    data = extractor("stories.csv")
    html = html_generator(data)
    with open('docs/index.html', 'w') as fh:
        fh.write(html)

main()