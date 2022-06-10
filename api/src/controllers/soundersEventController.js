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

// Get single soundersEvent by ID
exports.getSingleSoundersEvent = async (req, reply) => {
  try {
    const id = req.params.id
    const soundersEvent = await SoundersEvent.findById(id)
    return soundersEvent
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

// // Update an existing soundersEvent
// exports.updatesoundersEvent = async (req, reply) => {
//   try {
//     const id = req.params.id
//     const soundersEvent = req.body
//     const { ...updateData } = soundersEvent
//     const update = await soundersEvent.findByIdAndUpdate(id, updateData, { new: true })
//     return update
//   } catch (err) {
//     throw boom.boomify(err)
//   }
// }