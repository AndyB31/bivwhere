
import os
import time
import asyncio
from pyppeteer import launch

async def conversion(long, lat):

    browser = await launch(options={'args': ['--no-sandbox']})
    page = await browser.newPage()
    await page.goto(f'https://www.swisstopo.admin.ch/en/maps-data-online/calculation-services/navref.html', {"waitUntil" : "networkidle0"})

    #insert data and click etrf93
    time.sleep(2)

    await page.evaluate(f'''() => {{
      let el = document.querySelector('#input_frame')
      el.value = 'etrf93'
    }}''')

    await page.evaluate(f'''() => {{
      let el = document.querySelector('#input_e_d')
      el.value = '{long}'
    }}''')

    await page.evaluate(f'''() => {{
      let el = document.querySelector('#input_n_d')
      el.value = '{lat}'
    }}''')
    
    await page.evaluate('''() => {
        let el = document.querySelector('#calc_execute').click()
      }''')
    
    time.sleep(1)

    #retrieve data 

    e = await page.evaluate('''() => {
      let el = document.querySelector('#output_e').value
    }''')

    n = await page.evaluate('''() => {
      let el = document.querySelector('#output_n').value
    }''')
    
    await browser.close()

    print(e, n)
  
    return (e, n)
    

def conversion_loc(long, lat):
  return asyncio.get_event_loop().run_until_complete(conversion(long, lat))

