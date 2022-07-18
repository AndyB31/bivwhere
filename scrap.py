import os
import time
import asyncio
from pyppeteer import launch

async def main():

    e = "2608084.69"
    n = "1173727.56"

    dirname = f"E{e}N{n}"
    os.mkdir(dirname)

    browser = await launch()
    page = await browser.newPage()
    await page.goto(f'https://map.geo.admin.ch/?lang=en&topic=swisstopo&bgLayer=ch.swisstopo.pixelkarte-farbe&layers_opacity=0.75&E={e}&N={n}&zoom=8&catalogNodes=1436', {"waitUntil" : "networkidle0"})
    
    # remove header
    await page.evaluate('''() => {
      let elem = document.querySelector('#header');
      elem.parentNode.removeChild(elem);
    }''')

    # remove buttons bar
    await page.evaluate('''() => {
      let elem = document.querySelector('#buttonGroup');
      elem.parentNode.removeChild(elem);
    }''')

    # choose white background and remove background selector 
    await page.evaluate('''() => {
      let elem = document.querySelector('[ga-background-selector]');
      elem.querySelector('div[title="White background"]').click()
      elem.parentNode.removeChild(elem);
    }''')

    # remove watermark
    await page.evaluate('''() => {
      let elem = document.querySelector('[ga-attribution]');
      elem.parentNode.removeChild(elem);
    }''')

    # hide pulldown 
    await page.evaluate('''() => {
      let elem = document.querySelector('#pulldown');
      elem.style.display = "none"
    }''')

    # remove footer 
    await page.evaluate('''() => {
      let elem = document.querySelector('#footer');
      elem.parentNode.removeChild(elem);
    }''')


    #open pulldown to choose label

    await page.evaluate('''() => {
      let el = document.querySelector('label[title="Primary surfaces VECTOR25"]')
      if (!el) { 
        document.querySelector('a[title="Landscape models"]').click()
      }
    }''')

    await page.evaluate('''() => {
      let el = document.querySelector('label[title^="Slope classes over"]')
      if (!el) { 
        document.querySelector('a[title="Height models"]').click()
      }
    }''')
    

    # screenshot for Primary surfaces VECTOR25

    await page.evaluate('''() => {
      document.querySelector('label[title="Primary surfaces VECTOR25"]').click()
    }''')
    
    time.sleep(1)

    await page.screenshot({'path': f'{dirname}/map_vector_25.png'})

    await page.evaluate('''() => {
      document.querySelector('label[title="Primary surfaces VECTOR25"]').click()
    }''')

    # screenshot for Slope classes over 30°

    await page.evaluate('''() => {
      document.querySelector('label[title^="Slope classes over"]').click()
    }''')
    
    time.sleep(1)

    await page.screenshot({'path': f'{dirname}/map_slope_over_30.png'})

    await page.evaluate('''() => {
      document.querySelector('label[title^="Slope classes over"]').click()
    }''')
    
    # screenshot for Protected Areas swissTLMRegio 

    await page.evaluate('''() => {
      document.querySelector('label[title="Protected Areas swissTLMRegio"]').click()
    }''')

    time.sleep(1)
    
    await page.screenshot({'path': f'{dirname}/map_protected.png'})

    await page.evaluate('''() => {
      document.querySelector('label[title="Protected Areas swissTLMRegio"]').click()
    }''')

    # screenshot for Hiking trails

    await page.evaluate('''() => {
      document.querySelector('label[title="Hiking trails"]').click()
    }''')
    
    time.sleep(1)
    
    await page.screenshot({'path': f'{dirname}/map_hiking_trail.png'})

    await page.evaluate('''() => {
      document.querySelector('label[title="Hiking trails"]').click()
    }''')
    
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())