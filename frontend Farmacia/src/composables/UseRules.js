export const useRules = () => {
  const required = (value) => !!value || "Requerido";
  const requiredRule = (value) => !!value || "Requerido";
  const emailRule = (value) =>
    !value ||
    /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(value) ||
    "Email debe ser valido";

  return {
    required,
    requiredRule,
    emailRule,
  };
};
