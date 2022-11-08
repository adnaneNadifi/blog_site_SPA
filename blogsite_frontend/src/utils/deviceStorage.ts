import { LocalStorage } from 'quasar';

const deviceStorage = {
  saveKey(key: string, value: string) {
    LocalStorage.set(key, value);
  },
  retrieveKey(key: string) {
    try {
      return LocalStorage.getItem(key);
    } catch (error) {
      console.log(error);
      return '';
    }
  },
  destroyKey(key: string) {
    try {
      LocalStorage.remove(key);
    } catch (error) {
      console.log(error);
    }
  },
};
export default deviceStorage;
