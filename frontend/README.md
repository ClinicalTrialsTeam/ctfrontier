## Dependency management


### What is package.json?

`package.json` lists the dependencies of the project and defines the rules for
which versions of the dependencies will be allowed. There is a separate category
for app dependencies ("dependencies") vs development dependencies ("devDependencies").

`package.json` uses semantic versioning rules to define which updates can be
installed when `npm update` is run. For example, `^`, the most commonly
use rule, only allows updates that do not change the leftmost non-zero number.
For example, `^1.0.0` would allow updates to `1.1.1` but not to `2.0.0` and 
`^1.1.0` would allow updates to `1.1.1` but not `1.2.0`.


More details on npm semeantic versioning rules here: <https://nodejs.dev/learn/semantic-versioning-using-npm/>

### How do I install new dependencies?

To install new dependencies:

1. Make sure your docker container is running, or start it with `docker-compose up` or `docker-compose up react` to only run the react container.
1. Connect to the react docker container `docker exec -it react /bin/bash`
1. Install with `npm i <package-name> --save` for an app dependency or
`npm i <package-name> --save-dev` for a development dependency.


### What is package-lock.json?

`package-lock.json` Stores the versions of every dependency that are actually
being used by the application. This makes the results of running the app
reproducable. Running `npm update` will cause `package-lock.json`
to update if there are any new package versions available  that fit the rules
from `package.json` (there almost always are).

If you see the error below when running `npm install` or `npm update`,
you probably just need to add `--legacy-peer-deps` to your command.

    npm ERR! ERESOLVE unable to resolve dependency tree
    ....
    npm ERR! Could not resolve dependency:
    ...
    npm ERR! Fix the upstream dependency conflict, or retry
    npm ERR! this command with --force, or --legacy-peer-deps
    npm ERR! to accept an incorrect (and potentially broken) dependency resolution.


Periodically, `npm update` should be run to update the dependencies and the new `package-lock.json` file should be committed.

## Fixing ESLint errors

You can run ESLint from your terminal. First you should probably make sure
that you have an updated version of Node (this project currently recommends
at least version 15.4.0) and that you have ESLint installed.

Then, from the frontend folder you can run an ESLint check with `eslint .`.
You can automatically fix any ESLint problems that are automatically
fixable with `eslint --fix`.
(You can also automatically fix ESLint errors from your IDE)

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.\
You will also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can’t go back!**

If you aren’t satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you’re on your own.

You don’t have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn’t feel obligated to use this feature. However we understand that this tool wouldn’t be useful if you couldn’t customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)
