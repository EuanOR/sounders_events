// External Dependancies
const boom = require('boom')

// Get Data Models
const SoundersEvent = require('../models/SoundersEvent')

// Get all soundersEvents
exports.getSoundersEvents = async (req, reply) => {
  try {
    const soundersEvents = await SoundersEvent.find()
    return soundersEvents
  } catch (err) {
    throw boom.boomify(err)
  }
}

// Add a new soundersEvent
exports.addSoundersEvent = async (req, reply) => {
  try {
    const soundersEvent = new SoundersEvent(req.body)
    return soundersEvent.save()
  } catch (err) {
    throw boom.boomify(err)
  }
}