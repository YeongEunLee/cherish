module.exports = (sequelize, DataTypes) => {
    return sequelize.define('Water', {
        waterIdx: {
            type: DataTypes.INTEGER,
            primaryKey: true,
            allowNull: false,
        },
        waterDate: {
            type: DataTypes.DATE,
            allowNull: false,
        },
        review: {
            type: DataTypes.TEXT,
            allowNull: true,
        },
        goal: {
            type: DataTypes.DATE,
            allowNull: false,
        },
        postpone: {
            type: DataTypes.INTEGER,
            allowNull: true,
            defaultValue: 0,
        },
    }, {
        timestamps: false,
        underscored: true,
        tableName: 'water',
    })
}