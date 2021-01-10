module.exports = (sequelize, DataTypes) => {
  return sequelize.define(
    "Plant",
    {
      image_url: {
        type: DataTypes.STRING(100),
        allowNull: false,
      },
      name: {
        type: DataTypes.STRING(45),
        allowNull: false,
      },
    },
    {
      timestamps: false,
      underscored: false,
      tableName: "plant",
    }
  );
};
