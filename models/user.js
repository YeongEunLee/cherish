module.exports = (sequelize, DataTypes) => {
    return sequelize.define('User', {
        userIdx: {
            type: DataTypes.INTEGER,
            primaryKey: true,
            allowNull: false,
        },
        userName: {
            type: DataTypes.STRING(45),
            allowNull: false,
        },
        userId: {
            type: DataTypes.STRING(45),
            allowNull: false,
        },
        password: {
            type: DataTypes.STRING(100),
            allowNull: false,
        },
        salt: {
            type: DataTypes.STRING(100),
            allowNull: false,
        },
        userPhone: {
            type: DataTypes.STRING(45),
            allowNull: false,
        },
        userNickname: {
            type: DataTypes.STRING(45),
            allowNull: false,
        },
        userSex: {
            type: DataTypes.BOOLEAN,
            allowNull: false,
        },
        userBirth: {
            type: DataTypes.STRING(45),
            allowNull: false,
        },
        userProfileImageUrl: {
            type: DataTypes.STRING(100),
            allowNull: false,
        }
    }, {
        timestamps: false,
        underscored: true,
        tableName: 'user',
    })
}