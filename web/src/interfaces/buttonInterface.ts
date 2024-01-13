export default interface ButtonProps {
  label: string;
  type: string;
  className: string;
  onClick: (event: React.MouseEvent<HTMLButtonElement>) => void;
}