const BundleTracker = require('webpack-bundle-tracker')
const DEPLOYMENT_PATH = '/static/dist/'

module.exports = {
    "transpileDependencies": [
        "vuetify"
    ],
    pages: {
        main: {
            entry: 'src/main/index.js',
        },
        auth: {
            entry: 'src/auth/index.js',
        }
    },

    publicPath: process.env.NODE_ENV === 'production' ? DEPLOYMENT_PATH : 'http://localhost:8080/',
    outputDir: '../static/dist',

    devServer: {
        public: 'localhost:8080',
        headers: {
            'Access-Control-Allow-Origin': '*',
        },
    },
    chainWebpack: config => {
        config.optimization.splitChunks({
            cacheGroups: {
                common: {
                    name: 'chunk-vendor',
                    minChunks: 1,
                    priority: -10,
                    chunks: 'initial',
                    reuseExistingChunk: true
                }
            }
        })
    },

    configureWebpack: {
        plugins: [
            new BundleTracker({path: __dirname, filename: 'webpack-stats.json'}),
        ],
    },
}