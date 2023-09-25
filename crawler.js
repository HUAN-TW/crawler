const axios = require('axios')
const cheerio = require('cheerio')

// URL for the search query
const searchURL =
  'https://www.funtime.com.tw/oveticket/result.php?bfrom_city=TY&city=TYO_NRT&departure=2023-11-01&backdate=2023-11-05&type=ROU&airline%5B%5D=none&bclass=EC&forward%5B%5D=NSTOP&sort=price&order=up&lcc=on'

// Function to fetch and parse the page
async function searchFlights() {
  try {
    // Fetch the HTML content of the search results page
    const response = await axios.get(searchURL)

    // Load the HTML content into Cheerio for parsing
    const $ = cheerio.load(response.data)

    // You can now use jQuery-like syntax to extract information from the page
    // For example, let's extract all flight prices:
    const flightPrices = []
    $('span.price').each((index, element) => {
      const price = $(element).text().trim()
      flightPrices.push(price)
    })

    // Print the flight prices
    console.log('Flight Prices:')
    flightPrices.forEach((price, index) => {
      console.log(`${index + 1}: ${price}`)
    })
  } catch (error) {
    console.error('Error:', error)
  }
}

// Call the function to initiate the search
searchFlights()
