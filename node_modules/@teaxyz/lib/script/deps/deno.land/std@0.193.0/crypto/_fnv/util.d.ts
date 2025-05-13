export declare function swap32(val: number): number;
/**
 * mul32 performs 32-bit multiplication, a * b
 * @param a
 * @param b
 */
export declare function mul32(a: number, b: number): number;
/**
 * mul64 performs 64-bit multiplication with two 32-bit words
 * @param [ah, al]
 * @param [bh, bl]
 */
export declare function mul64([ah, al]: [number, number], [bh, bl]: [number, number]): [number, number];
