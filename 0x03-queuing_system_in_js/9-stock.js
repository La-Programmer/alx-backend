const util = require('util');
const express = require('express');
const redis = require('redis');


// VARIABLE DECLARATION
const app = express();
const port = 1245;
const redisClient = redis.createClient();
const listProducts = [
  {
    id: 1,
    name: 'Suitcase 250',
    price: 50,
    stock: 4
  },
  {
    id: 2,
    name: 'Suitcase 450',
    price: 100,
    stock: 10
  },
  {
    id: 3,
    name: 'Suitcase 650',
    price: 350,
    stock: 2
  },
  {
    id: 1,
    name: 'Suitcase 1050',
    price: 550,
    stock: 5
  }
]

// REDIS CLIENT HANDLING
redisClient.connect()
  .then(() => {
    console.log(`Successfully connected to redis server`);
  })
  .catch((err) => {
    console.log(`Error connecting to redis server: ${err}`);
  });

// EXPRESS APPLICATION ENDPOINTS
app.get('/list_products', (req, res) => {
  const response = [];
  for (const item of listProducts) {
    const responseItem = {
      itemId: item.id,
      itemName: item.name,
      price: item.price,
      initialAvailableQuantity: item.stock
    }
    response.push(responseItem); 
  }
  res.send(JSON.stringify(response));
});

app.get('/list_products/:itemId', (req, res) => {
  const itemId = req.params.itemId;
  const item = getItemById(itemId);
  getCurrentReservedStockById(itemId)
    .then((quantity) => {
      const response = {
        itemId: itemId,
        itemName: item.name,
        price: item.price,
        initialAvailableQuantity: item.stock,
        currentQuantity: quantity,
      }
      res.send(JSON.stringify(response));
    })
    .catch(() => {
      res.send(JSON.stringify({status: 'Product not found'}));
    })
});

app.get('/reserve_product/:itemId', (req, res) => {
  const itemId = req.params.itemId;
  const item = getItemById(itemId);
  if (item) {
    const itemStock = item.stock;
    if (itemStock >= 1) {
      reserveStockById(itemId, itemStock)
        .then(() => {
          res.send(JSON.stringify({
            status: 'Reservation confirmed',
            itemId: itemId
          }));
        })
        .catch((err) => {
          res.send(JSON.stringify({status: `Error: ${err}`}));
        });
    } else {
      res.send(JSON.stringify({
        status: 'Not enough stock available',
        itemId: itemId
      }));
    }
  } else {
    res.send(JSON.stringify({status: 'Product not found'}));
  }
});

app.listen(port, () => {
  console.log(`Application is running at port ${port}`);
});

// UTILITY FUNCTIONS
const getItemById = (id) => {
  for (const product of listProducts) {
    if (product.id == id) {
      return product;
    }
  }
};

const reserveStockById = async (itemId, stock) => {
  await redisClient.set(itemId, stock);
};


const getCurrentReservedStockById = async (itemId) => {
  const item = await redisClient.get(itemId);
  return item;
}
