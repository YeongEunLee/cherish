module.exports = (sequelize, DataTypes) => {
  return sequelize.define(
    "User",
    {
      name: {
        type: DataTypes.STRING(45),
        allowNull: false,
      },
      email: {
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
      phone: {
        type: DataTypes.STRING(45),
        allowNull: false,
      },
      nick_name: {
        type: DataTypes.STRING(45),
        allowNull: false,
      },
      sex: {
        type: DataTypes.BOOLEAN,
        allowNull: false,
      },
      birth: {
        type: DataTypes.STRING(45),
        allowNull: false,
      },
      profile_image_url: {
        type: DataTypes.STRING(100),
        allowNull: false,
      },
    },
    {
      timestamps: false,
      underscored: false,
      tableName: "user",
    }
  );
};
