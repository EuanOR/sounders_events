// Import our Controller
const soundersEventController = require('../controllers/soundersEventController')

const routes = [
  {
    method: 'GET',
    url: '/api/soundersEvents',
    handler: soundersEventController.getSoundersEvents
  },
  {
    method: 'GET',
    url: '/api/soundersEvents/:id',
    handler: soundersEventController.getSingleSoundersEvent
  },
  {
    method: 'POST',
    url: '/api/soundersEvents',
    handler: soundersEventController.addSoundersEvent
  }
    // schema: documentation.addSoundersEventSchema
  // {
  //   method: 'PUT',
  //   url: '/api/soundersEvents/:id',
  //   handler: soundersEventController.updatesoundersEvent
  // }
]
module.exports = routes