module.exports = (sequelize, DataTypes) => {
    return sequelize.define('Plant', {
        plantIdx: {
            type: DataTypes.INTEGER,
            primaryKey: true,
            allowNull: false,
        },
        plantImageUrl: {
            type: DataTypes.STRING(100),
            allowNull: false,
        },
        plantName: {
            type: DataTypes.STRING(45),
            allowNull: false,
        }
    }, {
        timestamps: false,
        underscored: true,
        tableName: 'plant',
    })
}