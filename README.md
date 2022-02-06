# Money Maker Scam (for educational purposes)

- Load the development dependencies electron and electron-builder: `npm install`
- Run it in dev mode to make sure it works: `npm run start`
- Add your own MacAppStore.provisionprofile to the project's build directory.
- Add your own TeamID.appID in the entitlements.mas.plist file on line 9.
- In the package.json file at a minimum change the name and appId properties to your information.
- Build the app for the mac app store: `electron-builder --mac`
