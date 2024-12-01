# BlackHole Audio Routing

## Scenario: Route browser audio and external microphone audio to Zoom

The flows below will look like these:

- Browser audio → System Output → Multi-Output Device → [splits to both]:
  - → BlackHole → Zoom
  - → Regular Output (speakers/headphones)
- External Mic → Aggregate Device → GarageBand → BlackHole → Zoom

- Install [BlackHole Audio Routing](https://existential.audio/blackhole). Most probably you only need to install BlackHole 2ch.

## Setup Multi-Output Device

The Multi-Output Device is created to combine BlackHole and the External Microphone.

1. Open Audio MIDI Setup using Spotlight (Command+Space)
2. Create a Multi-Output Device:
   - Click the + button in the bottom left corner
   - Select "Create Multi-Output Device"
   - Add BlackHole and enable drift compensation
   - Add External Microphone, choose this as the primary device, don't enable drift compensation for this one
   - Right-click on the Multi-Output Device and select "Add Output Device"

Tidbits on drift compensation and clock source:

- Drift compensation: Used to synchronize audio streams from different devices, preventing audio drift over time.
- Not enabled for primary device: The primary device (External Microphone) acts as the master clock, so it doesn't need compensation.
- Clock source set to primary device: Ensures all other devices sync to the External Microphone's timing, maintaining consistent audio across all sources.

## Create Aggregate Device

Recall an aggregate device is a device that has multiple inputs and outputs. The Aggregate Device combines the microphone and BlackHole inputs

Note: When you create this device, GarageBand will ask you to enable it. There will be three input devices available in GarageBand:

- 1 (Aggregate Device) is from BlackHole 2ch
- 2 (Aggregate Device) is also from BlackHole 2ch
- 3 (Aggregate Device) is from External Microphone

1. Open Audio MIDI Setup from Utilities folder
2. Click the + button in the bottom left
3. Select "Create Aggregate Device"
4. Enable both your microphone and BlackHole by checking their boxes
5. Set your main microphone as the Clock Source
6. Enable Drift Correction for BlackHole

## GarageBand Setup

1. Open GarageBand and create an Empty Project
2. Create one audio track:
   - Set input to "3 (Aggregate Device)"
3. Enable monitoring (orange button)
4. Open GarageBand Preferences → Audio/MIDI
5. Set Output Device to BlackHole 2ch

## Setup Zoom

1. Set the Zoom audio input device to "BlackHole 2ch"
2. Set the Zoom audio output device to "Multi-Output Device"
