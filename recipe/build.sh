OMPATH=${PREFIX}/lib/omlibrary
mkdir -p ${OMPATH}
cp -R ${SRC_DIR}/Complex.mo ${OMPATH}/"Complex ${PKG_VERSION}.mo"
cp -R ${SRC_DIR}/Modelica ${OMPATH}/"Modelica ${PKG_VERSION}"
cp -R ${SRC_DIR}/ModelicaServices ${OMPATH}/"ModelicaServices ${PKG_VERSION}"
