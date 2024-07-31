export const useValidationError = (errorCode) => {
  const codeMatcher = {
    ERR_NETWORK: "Error de conexion con el servidor",
    ERR_CONNECTION_REFUSED: "Error de conexion con el servidor",
    ERR_CONNECTION_RESET: "Error de conexion con el servidor",
  };

  return codeMatcher[errorCode];
};
