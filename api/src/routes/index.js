// Import our Controller
const soundersEventController = require('../controllers/soundersEventController')

const routes = [
  {
    method: 'GET',
    url: '/soundersEvents',
    handler: soundersEventController.getSoundersEvents
  },
  {
    method: 'POST',
    url: '/soundersEvents',
    handler: soundersEventController.addSoundersEvent
  }

]
module.exports = routes