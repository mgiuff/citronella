const request = require('request')

const url = 'https://api.darksky.net/forecast/7beb135b2f4baf002c7c260862cc2573/41.8782,12.5281'

request({ url: url }, (error, response) => {
    const data = JSON.parse(response.body)
    console.log(data.currently)
})
