// External Dependancies
const mongoose = require('mongoose')

const soundersEventSchema = new mongoose.Schema({
  name: String,
  date: Date,
  venue: String,
  address: String,
  city: String,
  state: String,
  zip: String,
  country: String
})

module.exports = mongoose.model('SoundersEvent', soundersEventSchema)