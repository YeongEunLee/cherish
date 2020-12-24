module.exports = (sequelize, DataTypes) => {
    return sequelize.define('Cherish', {
        cherishIdx: {
            type: DataTypes.INTEGER,
            primaryKey: true,
            allowNull: false,
        },
        cherishName: {
            type: DataTypes.STRING(45),
            allowNull: false,
        },
        cherishBirth: {
            type: DataTypes.DATE,
            allowNull: false,
        },
        cherishPhone: {
            type: DataTypes.STRING(45),
            allowNull: false,
        },
        cycleDate: {
            type: DataTypes.DATE,
            allowNull: false,
        },
        startDate: {
            type: DataTypes.DATE,
            allowNull: false,
        },
        noticeTime: {
            type: DataTypes.STRING(45),
            allowNull: false,
        }
    }, {
        timestamps: false,
        underscored: true,
        tableName: 'cherish',
    })
}