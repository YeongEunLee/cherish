const Sequelize = require('sequelize');
const env = process.env.NODE_ENV || 'development';
const config = require(__dirname + '/../config/config.json')[env];
const db = {};

let sequelize;
if (config.use_env_variable) {
  sequelize = new Sequelize(process.env[config.use_env_variable], config);
} else {
  sequelize = new Sequelize(config.database, config.username, config.password, config);
}

db.User = require('./user')(sequelize, Sequelize);
db.Cherish = require('./cherish')(sequelize, Sequelize);
db.Plant = require('./plant')(sequelize, Sequelize);
db.Water = require('./water')(sequelize, Sequelize);

/** 1 : N User : Cherish */
db.User.hasMany(db.Cherish, { onDelete: 'cascade', foreignKey: 'userIdx', sourceKey: 'userIdx'});
db.Cherish.belongsTo(db.User, {foreignKey: 'userIdx', targetKey: 'userIdx'});
/** 1 : N Plant : Cherish */
db.Plant.hasMany(db.Cherish, { onDelete: 'cascade', foreignKey: 'plantIdx', sourceKey: 'plantIdx'});
db.Cherish.belongsTo(db.Plant, { foreignKey: 'plantIdx', targetKey: 'plantIdx'});
/** 1 : N Cherish : Water */
db.Cherish.hasMany(db.Water, { onDelete: 'cascade', foreignKey: 'cherishIdx', sourceKey: 'cherishIdx'});
db.Water.belongsTo(db.Cherish, { foreignKey: 'cherishIdx', targetKey: 'cherishIdx'});

db.sequelize = sequelize;
db.Sequelize = Sequelize;

module.exports = db;
