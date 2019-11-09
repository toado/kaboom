#rottentomatoes
from bs4 import BeautifulSoup

# normally use a request
website =''' <!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <title>Coffee Time</title>
  </head>
  <body>
    <!-- Extra logo with clickable url -->
    <a href="https://www.google.ca/" target="_blank"
      ><img src="./images/Coffee_Logo.webp" id="logo" alt="Coffe Logo"
    /></a>
    <!-- <img src="./images/Coffee_Logo.webp" id="logo" alt="Coffe Logo" /> -->
    <h1>Coffee By Byron</h1>
    <ul>
      <li><a href="index.html">Home</a></li>
      <li><a href="about.html">About</a></li>
      <li><a href="numbers.html">Numbers</a></li>
      <li><a href="contact.html">Contact</a></li>
    </ul>
    <img
      src="./images/backgroundcoffee.jpeg"
      width="100%"
      alt="Background Coffee"
    />
    <br />
    <h1>Featured Products</h1>
    <h2>Dark Roast</h2>
    <img src="./images/coffee1.jpeg" alt="Dark Roast" />
    <p hg>
      Lorem, ipsum dolor sit amet consectetur adipisicing elit. Obcaecati
      explicabo nemo iure neque magni suscipit, iste aut nulla nam quo corrupti
      perspiciatis incidunt tenetur, vero consequatur. Iste excepturi magni
      itaque nesciunt quasi minus, libero repellendus iusto cum obcaecati
      laboriosam nobis officia aliquam possimus repudiandae iure consectetur at
      accusamus modi nisi perspiciatis deserunt quaerat recusandae! Alias
      accusantium magni tenetur quaerat voluptates eaque deserunt exercitationem
      molestiae perspiciatis beatae nihil perferendis iure numquam libero
      reprehenderit, nostrum dolorem odit est dignissimos magnam nemo doloribus
      nesciunt. Obcaecati aspernatur consequatur accusantium odit adipisci. A
      porro perspiciatis facilis illum provident rerum sit, inventore vitae
      dolores maxime delectus.
    </p>
    <h4><a href="https://www.wikipedia.org" target="_blank">Details</a></h4>
    <h2>Steeped Tea</h2>
    <img src="./images/coffee2.jpeg" alt="Steeped Tea" />
    <p>
      Lorem, ipsum dolor sit amet consectetur adipisicing elit. Commodi, sequi.
      Saepe eum explicabo unde reiciendis inventore temporibus magnam,
      voluptatem accusamus, autem beatae necessitatibus deleniti tempora
      blanditiis repellendus iure voluptatum itaque repudiandae, id mollitia
      asperiores quis nobis? Soluta, illum. Quaerat, aut. Nam deserunt excepturi
      consequatur ad perspiciatis, aperiam consequuntur alias obcaecati vero
      expedita assumenda illo! Autem possimus deleniti laboriosam, eum iusto
      praesentium. Necessitatibus, nisi sapiente earum atque enim excepturi
      iste? Illo consequatur doloribus magnam voluptas nostrum eos perspiciatis
      quo id nisi! Ea nemo vitae adipisci optio facilis reprehenderit. Animi,
      minima sapiente, asperiores assumenda modi deleniti dignissimos eaque
      distinctio voluptas atque aspernatur.
    </p>
    <h4><a href="https://www.wikipedia.org" target="_blank">Details</a></h4>
    <h2>Cappuccino</h2>
    <img src="./images/coffee3.jpeg" alt="Cappuccino" />
    <p>
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Odio assumenda
      perspiciatis illum doloribus officia vitae blanditiis doloremque harum,
      neque minima fugit sequi nostrum vel fugiat, dolor iusto repudiandae
      beatae eum tempore dignissimos odit voluptatibus quaerat temporibus
      cumque! Voluptatibus natus libero omnis cupiditate facere aspernatur
      fugiat, quibusdam quia architecto soluta adipisci vero, doloremque fuga
      ducimus nesciunt molestiae aliquam harum deserunt quasi sapiente sint nam!
      A magnam porro debitis aliquid corporis assumenda, neque dicta asperiores
      harum vitae sed rem inventore. Expedita asperiores fugiat maiores. Labore
      libero, ratione ab praesentium, dolores harum non, eos nisi quisquam
      excepturi magnam voluptas facilis dolorum quod commodi.
    </p>
    <h4><a href="https://www.wikipedia.org" target="_blank">Details</a></h4>
    <br />
    <br />
    <br />
    <br />
    <br />
    <br />
    <br />
    <br />
    <br />
    <br />
    <br />
    <br />
    <br />
    <br />
    <br />
    <p>copyright &copy; 2019</p>
    <h3><a href="#logo">Back to the top</a></h3>
  </body>
</html>
'''

#website information, how to parse
soup = BeautifulSoup(website, 'html.parser')

#directly normally dont use this
#print(soup.body)
#print(soup.head)
#print(soup.title)

#find()
#el = soup.find('title')

# find_all() or findAll() they are the same
#el = soup.find_all("p")
#print (el)

#el = soup.find(id = '')
#el = soup.find(class_ = 'items')

#el = soup.find(attrs={"data-hello": "hi"})

# selecting of css: select is list, index to get string
#el = soup.select("#section-1")
#el = soup.select(".items")[0]

# get_text()
#el = soup.find(class_ = "item").get_text()

for item in soup.select()